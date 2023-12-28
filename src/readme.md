# Código principal

## Documentação online

A documentação do código criado pode ser [acessado online](https://gregoriofornetti.github.io/projeto-cg/docs/_build/html/index.html)

## Organização arquivos

O código ficou organizado nos seguintes repositórios e arquivos:

- **main.py**: código principal. Ao executa-lo, o usuário pode escolher a configuração a qual serão gerados os frames, quantos subprocessos serão criados (para aproveitar o paralelismo e usar a capacidade máxima da CPU) e quais frames serão feitos nessa execução. Todos os frames gerados serão armazenados em `animation_frames` (a partir do repositório principal do projeto).
- **resolutions.py:** código contendo as configurações de qualidade das animações disponíveis no sistema. Define as configurações que poderão ser utilizadas em: `main.py`, `generate_videos.py` e `verify_remaining_frames.py`
- **lib:** todos os arquivos das atividades passadas estão disponíveis nesse subdiretório. Este diretório possui todo código necessário para o funcionamento do código principal `Animation.py`. Mais sobre os códigos disponibilizados aqui pode ser verificado na [documentação online](https://gregoriofornetti.github.io/projeto-cg/docs/_build/html/index.html).
- **Animation.py:** código para gerar os frames da animação, utilizado pelo `main.py`. Toda a lógica de movimentação e da animação em si está nesse arquivo.
- **generate_videos.py:** gera os vídeos a partir dos frames gerados pela execução do código principal. É gerado um vídeo para cada resolução e um vídeo final compilando todas as animações, em todas as configurações. Armazena os vídeos em `animations` (a partir do código principal)
- **verify_remaining_frames.py:** informa quais frames ainda faltam ser gerados para cada configuração de animação.
- **teste.ipynb:** notebook usado para testar a implementação de `Animation.py`. O código final de `Animation.py` foi baseado neste notebook.
