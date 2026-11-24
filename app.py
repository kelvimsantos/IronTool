#!/usr/bin/env python3
"""Render entry point for IronTool's AGPL-licensed Barehands web app."""
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
import importlib.util
import json
import os
import sys

ROOT = Path(__file__).resolve().parent
UPSTREAM = ROOT / ".build" / "barehands"
SERVER_FILE = UPSTREAM / "server.py"
if not SERVER_FILE.is_file():
    raise SystemExit("Barehands source is missing. Run build.sh before starting the service.")

spec = importlib.util.spec_from_file_location("barehands_server", SERVER_FILE)
barehands = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = barehands
spec.loader.exec_module(barehands)

class RenderHandler(barehands.Handler):
    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/_health":
            body = json.dumps({"status": "ok"}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if path in ("", "/"):
            self.send_response(302)
            self.send_header("Location", "/stage.html")
            self.end_headers()
            return
        if path == "/stage.html":
            # AGPL source offer: keep a prominent link to this deployment's
            # corresponding source, alongside the upstream project source.
            page = (UPSTREAM / "stage.html").read_text(encoding="utf-8")
            notice = ('''<a href="https://github.com/kelvimsantos/IronTool/tree/barehands-adaptacao" '''
                      '''style="position:fixed;z-index:2000;left:8px;bottom:8px;''' 
                      '''padding:7px 10px;border-radius:8px;background:#062923;''' 
                      '''color:#9ff0dd;font:12px sans-serif;opacity:.85" '''
                      '''aria-label="Código-fonte desta versão (AGPL-3.0-or-later)">''' 
                      '''Código-fonte (AGPL)</a>''')
            page = page.replace("</body>", notice + "</body>", 1)
            body = page.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    print(f"IronTool/Barehands listening on 0.0.0.0:{port}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", port), RenderHandler).serve_forever()
