# Atividades de computação gráfica

Repositório contendo o trabalho final da disciplina de computação gráfica (2023/2) , ministrada pelo professor Mario Liziér.

Alunos: 

Guilherme Fumagali Marques - RA: 792182
Gregório Fornetti Azevedo - RA: 792181
Vinicius Gabriel Nanini da Silva - RA: 795181
Rodrigo Henrique Amaral Araujo - RA: 792241

## Descrição do trabalho

O objetivo desta atividade é o desenvolvimento de uma animação utilizando as implementações desenvolvidas em aula.

O projeto deve gerar uma animação com pelo menos 5 segundos. Como a implementação não é otimizada e não temos muito poder de processamento, a animação pode ter uma baixa resolução e poucos quadros por segundo. A composição dos quadros pode ser realizada com ferramenta externa (exportando em um formato avi/mp4/etc), mas a geração das imagens deve utilizar as implementações dos membros do grupo.

Utilize pelo menos 3 objetos, sendo pelo menos um deles formado por triângulos. Utilize materiais difusos e reflexivos. Faça pelo menos um movimento com a câmera e outro com pelo menos um dos objetos.

O projeto será avaliado considerando os seguinte requisitos:
- Atendimento aos requisitos;
- Documentação do código e de apesentação do projeto;
- Qualidade visual final da animação;

## Detalhes sobre a implementação



### Principais bibliotecas utilizadas no projeto

- [NumPy](https://numpy.org/): fornece estruturas de dados (arrays) e operações sobre elas que serão úteis para manipular e gerar as imagens.
- [Pillow](https://pypi.org/project/Pillow/): para salvar e ler imagens em diversos formatos.
- [Sphinx](https://www.sphinx-doc.org/pt_BR/master/): gerador de documentação a partir dos comentários de documentação incluídos no próprio código.
- [tqdm](https://tqdm.github.io/): para indicar progresso das operações/funções mais demoradas.

### Instalação

Para conseguir executar o projeto, é necessário ter instalado o Python e todas as bibliotecas citadas. Para instalar mais facilmente as bibliotecas necessárias, foi criado o arquivo `requirements.txt`, e utilizando o pip (sistema de gerenciamento de pacotes do Python), é possível instalar todas as bibliotecas usando o comando `pip install -r requirements.txt`


## Sobre geração de documentação usando Sphinx

Para usar o gerador de documentação Sphinx, foi seguido o [tutorial do canal Learn Programming with Joel](https://www.youtube.com/watch?v=BWIrhgCAae0)

Comandos necessários para gerar a página de documentação:

1- Para gerar alguns arquivos necessários para a geração da documentação, execute o comando:

```
sphinx-apidoc -o docs .
```

2- Para de fato gerar a documentação, execute o comando:

```
docs/create.bat html
```

A documentação gerada será salva no caminho `docs/_build/html`, podendo ser vizualizada no arquivo `index.html`

3- Em alguns casos, a documentação pode parecer desatualizada. Isso pode acontecer quando os arquivos gerados na etapa 1 já tinham sido criados antes,
e não foram atualizados nessa atualização. Para atualiza-los, é preciso exclui-los e depois criar novamente com o comando da etapa 1. No geral,
para excluir os arquivos que precisam ser atualizados, execute os comandos:

```
rm docs/modules.rst
rm docs/Atividade<NUM_ATIVIDADE>.rst
```
