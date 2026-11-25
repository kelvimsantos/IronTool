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

BROWSER_PANEL = r'''<style>
#it-browser-launcher{position:fixed;right:14px;top:14px;z-index:2100;border:1px solid rgba(143,240,228,.7);border-radius:999px;background:rgba(4,28,30,.88);color:#dffff8;padding:11px 16px;font:600 14px system-ui;cursor:pointer;box-shadow:0 4px 20px #0008;touch-action:manipulation}
#it-browser-panel{position:fixed;z-index:2101;left:5vw;top:6vh;width:90vw;height:86vh;max-width:1100px;max-height:850px;display:none;flex-direction:column;overflow:hidden;border:1px solid rgba(143,240,228,.72);border-radius:16px;background:rgba(5,20,23,.97);box-shadow:0 16px 55px #000a;color:#ecfffa;font:14px system-ui}
#it-browser-panel.open{display:flex}
#it-browser-toolbar{display:flex;align-items:center;gap:8px;padding:10px;border-bottom:1px solid #6fe3c955}
#it-browser-url{flex:1;min-width:0;height:40px;padding:0 12px;border:1px solid #6fe3c977;border-radius:8px;background:#071719;color:#fff;font-size:15px}
#it-browser-panel button{border:1px solid #6fe3c988;border-radius:8px;background:#103337;color:#eafffb;padding:9px 12px;font-size:14px;cursor:pointer;touch-action:manipulation}
#it-browser-panel button:hover,#it-browser-launcher:hover{background:#18504d}
#it-browser-help{margin:0;padding:7px 12px;color:#b9d8d1;background:#0b2426;font-size:12px}
#it-browser-frame{flex:1;width:100%;min-height:0;border:0;background:#fff}
@media(max-width:600px){#it-browser-panel{left:2vw;top:8vh;width:96vw;height:84vh}#it-browser-toolbar{gap:5px;padding:7px}#it-browser-panel button{padding:9px 8px;font-size:12px}#it-browser-url{font-size:13px}}
</style>
<button id="it-browser-launcher" type="button" aria-controls="it-browser-panel">Abrir navegador</button>
<section id="it-browser-panel" aria-label="Navegador sobre a câmera" aria-hidden="true">
  <div id="it-browser-toolbar">
    <input id="it-browser-url" type="url" inputmode="url" autocomplete="url" spellcheck="false" aria-label="Endereço HTTPS" placeholder="https://exemplo.com">
    <button id="it-browser-go" type="button">Ir</button>
    <button id="it-browser-newtab" type="button">Nova aba</button>
    <button id="it-browser-close" type="button" aria-label="Fechar navegador">Fechar</button>
  </div>
  <p id="it-browser-help">Use um endereço HTTPS. Alguns sites impedem a exibição incorporada; nesse caso, tente “Nova aba”. A navegação por gestos dentro da página não está habilitada nesta versão.</p>
  <iframe id="it-browser-frame" title="Página web sobre a câmera" sandbox="allow-forms allow-scripts allow-popups" referrerpolicy="no-referrer"></iframe>
</section>
<script>
(() => {
  const launcher = document.getElementById('it-browser-launcher');
  const panel = document.getElementById('it-browser-panel');
  const input = document.getElementById('it-browser-url');
  const frame = document.getElementById('it-browser-frame');
  let currentUrl = '';

  function normalizedUrl() {
    let value = input.value.trim();
    if (!value) throw new Error('Digite um endereço HTTPS.');
    if (!/^[a-z][a-z0-9+.-]*:/i.test(value)) value = 'https://' + value;
    const parsed = new URL(value);
    if (parsed.protocol !== 'https:') throw new Error('Por segurança, use um endereço HTTPS.');
    return parsed.href;
  }

  function navigate() {
    try {
      currentUrl = normalizedUrl();
      input.value = currentUrl;
      frame.src = currentUrl;
      document.getElementById('it-browser-help').textContent = 'Se o site bloquear a exibição incorporada, use “Nova aba”. Navegação por gestos dentro da página não está habilitada nesta versão.';
    } catch (error) {
      document.getElementById('it-browser-help').textContent = error.message;
      input.focus();
    }
  }

  function openPanel() {
    panel.classList.add('open');
    panel.setAttribute('aria-hidden', 'false');
    launcher.hidden = true;
    input.focus();
  }

  function closePanel() {
    panel.classList.remove('open');
    panel.setAttribute('aria-hidden', 'true');
    launcher.hidden = false;
    frame.src = 'about:blank';
  }

  launcher.addEventListener('click', openPanel);
  document.getElementById('it-browser-go').addEventListener('click', navigate);
  input.addEventListener('keydown', event => {
    if (event.key === 'Enter') navigate();
    if (event.key === 'Escape') closePanel();
  });
  document.getElementById('it-browser-close').addEventListener('click', closePanel);
  document.getElementById('it-browser-newtab').addEventListener('click', () => {
    try {
      currentUrl = normalizedUrl();
      input.value = currentUrl;
      window.open(currentUrl, '_blank', 'noopener,noreferrer');
    } catch (error) {
      document.getElementById('it-browser-help').textContent = error.message;
    }
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && panel.classList.contains('open')) closePanel();
  });
})();
</script>'''

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
            notice = ('''<a href="https://github.com/kelvimsantos/IronTool/tree/feature/camera-browser-panel" '''
                      '''style="position:fixed;z-index:2000;left:8px;bottom:8px;'''
                      '''padding:7px 10px;border-radius:8px;background:#062923;'''
                      '''color:#9ff0dd;font:12px sans-serif;opacity:.85" '''
                      '''aria-label="Código-fonte desta versão (AGPL-3.0-or-later)">'''
                      '''Código-fonte (AGPL)</a>''')
            page = page.replace("</body>", BROWSER_PANEL + notice + "</body>", 1)
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
