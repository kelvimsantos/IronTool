# IronTool — interface de mãos livres em 3D

Este repositório prepara o [Barehands](https://github.com/jaredrhod/barehands), de Jared Rhodenizer, para ser publicado como um serviço web no Render. O build baixa o projeto original e inclui os arquivos versionados na pasta `media/` deste repositório.

## Publicar no Render

1. Acesse [Render](https://render.com) e escolha **New → Blueprint**.
2. Conecte `kelvimsantos/IronTool` e selecione a branch `barehands-adaptacao`.
3. O Render detecta `render.yaml` e configura o serviço web. Confirme a criação.
4. Quando o deploy terminar, abra o endereço HTTPS gerado pelo Render no Chrome do tablet e permita o acesso à câmera.

A raiz do serviço encaminha para `/stage.html`. Não é necessário instalar Termux nem executar comandos no tablet. O app usa a câmera no navegador; o servidor do Render não acessa os arquivos privados do aparelho.

## Como adicionar imagens e modelos 3D

Adicione os arquivos ao repositório IronTool, dentro de `media/`. O nome das pastas determina como cada item aparece na tela:

| Pasta | Tipos aceitos | Aparência |
|---|---|---|
| `media/misc/` | `.png`, `.jpg`, `.jpeg`, `.webp`, `.gif` | Imagem em cartão de vidro |
| `media/fx/` | PNG transparente e `.webm` com transparência | Objeto flutuante sem moldura; vídeos repetem sem áudio |
| `media/models/` | `.glb`, `.gltf` | Modelo 3D com materiais e texturas |
| `media/holo/` | `.glb`, `.gltf` | Modelo 3D com aparência holográfica azul |

Exemplo de organização:

```text
media/
├── misc/
│   ├── ferramenta.png
│   └── referencia.jpg
├── fx/
│   └── chama-transparente.png
├── models/
│   └── peca-3d.glb
└── holo/
    └── projeto-holograma.glb
```

**Como enviar pelo GitHub no tablet ou computador:** abra o repositório, navegue até a pasta desejada (ou crie-a enviando um arquivo), use **Add file → Upload files**, selecione os arquivos, e faça o commit na branch `barehands-adaptacao`. O GitHub não mantém pastas vazias: cada pasta precisa conter pelo menos um arquivo. Use nomes simples, sem acentos ou espaços, por exemplo `chama-azul.png`.

Depois do commit, o Render deve iniciar um novo deploy automaticamente. Se não iniciar, abra o serviço no Render e use **Manual Deploy → Deploy latest commit**. Os itens aparecem na estante Props do app após a publicação. O app carrega os formatos listados acima; arquivos colocados em pastas com nomes diferentes podem não aparecer ou receber o visual esperado.

### Importante sobre armazenamento

Os arquivos em `media/` são incluídos no deploy a partir do Git. O disco do serviço Render pode ser temporário: arquivos enviados ou criados em tempo de execução não são uma forma confiável de armazenamento persistente e podem desaparecer em um novo deploy/reinício. Para adicionar ou atualizar itens, faça commit dos arquivos no repositório. Evite enviar arquivos privados, grandes ou protegidos por direitos autorais sem autorização.

## Notas e pastas de Markdown

O Barehands original também oferece uma estante de notas com arquivos `.md` configurados em `barehands.json`. Nesta integração hospedada, a configuração e as notas devem existir no ambiente do app; pastas locais do tablet não ficam acessíveis automaticamente ao serviço. Para apresentar imagens e modelos da pasta `media/`, use a estante Props.

## Executar localmente

```bash
bash build.sh
python app.py
```

Abra `http://localhost:10000/` no Chrome e permita o acesso à câmera. A primeira inicialização precisa de internet para obter MediaPipe e three.js dos CDNs usados pelo app.

## Código-fonte e licença

Esta adaptação é baseada em Barehands, Copyright (C) Jared Rhodenizer, licenciada sob **GNU AGPL-3.0-or-later**. O código desta integração está neste repositório; o código upstream está em [jaredrhod/barehands](https://github.com/jaredrhod/barehands). A interface publicada inclui um link para o código-fonte desta adaptação.
