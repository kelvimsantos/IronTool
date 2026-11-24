# IronTool — interface de mãos livres em 3D

Este repositório prepara o [Barehands](https://github.com/jaredrhod/barehands), de Jared Rhodenizer, para ser publicado como um serviço web no Render. O código original é baixado durante o build para `.build/barehands`; não é um fork nem uma cópia vendorizada no Git. A versão original e o histórico permanecem no repositório do autor.

## Publicar no Render

1. Acesse [Render](https://render.com) e escolha **New → Blueprint**.
2. Conecte `kelvimsantos/IronTool` e selecione a branch `barehands-adaptacao`.
3. O Render detecta `render.yaml` e configura o serviço web. Confirme a criação.
4. Quando o deploy terminar, abra o endereço HTTPS gerado pelo Render no Chrome do tablet e permita o acesso à câmera.

O build busca o Barehands upstream, e o servidor Python usa a variável `PORT` do Render e escuta em `0.0.0.0`. A raiz do serviço encaminha para `/stage.html`. Não é necessário instalar Termux nem executar comandos no tablet.

## Executar localmente

```bash
bash build.sh
python app.py
```

Abra `http://localhost:10000/` no Chrome. O navegador solicitará permissão para a câmera. A primeira inicialização precisa de internet para obter MediaPipe e three.js dos CDNs usados pelo app.

## O que o app oferece

Rastreamento de mãos pela câmera para mover cartões, imagens e modelos 3D por gestos. Os arquivos e notas disponíveis dependem dos recursos incluídos no checkout do Barehands feito no build. O serviço no Render não consegue acessar diretamente os arquivos privados armazenados no tablet; upload/armazenamento de arquivos não foi adicionado nesta adaptação.

## Código-fonte e licença

Esta adaptação é baseada em Barehands, Copyright (C) Jared Rhodenizer, licenciada sob **GNU AGPL-3.0-or-later**. O código desta integração está neste repositório; o código upstream está em [jaredrhod/barehands](https://github.com/jaredrhod/barehands). A interface publicada inclui um link para o código-fonte desta adaptação. MediaPipe e three.js são carregados dos CDNs definidos pelo projeto original.
