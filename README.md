# IronTool

Interface web com rastreamento de mãos pela câmera, adaptada para deployment em [Render](https://render.com).

## Executar localmente

```bash
python server.py
```

Abra `http://localhost:8794/stage.html` no Chrome e permita o acesso à câmera.

## Deploy no Render

1. Conecte este repositório ao Render.
2. Selecione **Web Service**.
3. Runtime: **Python**.
4. Build Command: `pip install -r requirements.txt`.
5. Start Command: `python server.py`.

## Licença

Adaptado de [barehands](https://github.com/jaredrhod/barehands), licenciado sob GNU AGPL-3.0-or-later.
