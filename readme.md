# Atividades de computação gráfica

Repositório contendo o trabalho final da disciplina de computação gráfica (2023/2) , ministrada pelo professor Mario Liziér.

Alunos: 

Guilherme Fumagali Marques - RA: 792182

Gregório Fornetti Azevedo - RA: 792181

Vinicius Gabriel Nanini da Silva - RA: 795181

Rodrigo Henrique Amaral Araujo - RA: 792241

## Descrição original do trabalho

O objetivo desta atividade é o desenvolvimento de uma animação utilizando as implementações desenvolvidas em aula.

O projeto deve gerar uma animação com pelo menos 5 segundos. Como a implementação não é otimizada e não temos muito poder de processamento, a animação pode ter uma baixa resolução e poucos quadros por segundo. A composição dos quadros pode ser realizada com ferramenta externa (exportando em um formato avi/mp4/etc), mas a geração das imagens deve utilizar as implementações dos membros do grupo.

Utilize pelo menos 3 objetos, sendo pelo menos um deles formado por triângulos. Utilize materiais difusos e reflexivos. Faça pelo menos um movimento com a câmera e outro com pelo menos um dos objetos.

O projeto será avaliado considerando os seguinte requisitos:
- Atendimento aos requisitos;
- Documentação do código e de apesentação do projeto;
- Qualidade visual final da animação;

## Animação proposta

Consistirá em uma cena com quatro objetos diferentes. Um cubo metálico (reflexivo) no centro da cena com duas esferas difusas próximos a ele. Há também uma grande esfera logo abaixo desses três objetos, simulando um piso. As duas esferas rotacionam ao redor do cubo reflexivo. A câmera está posicionada um pouco acima dos objetos, e esta rotaciona ao redor do cubo também (só que mais distante do que as duas esferas), sempre olhando para o centro da cena, onde está posicionado o cubo.

Além disso, a animação foi gerada em diversas configurações de qualidade diferentes para fazer um comparativo. Cada configuração possui valores diferentes para os seguintes atributos:

- **Largura:** quantidade de pixel em largura (número de pixels por linha)
- **Altura:** quantidade de pixel em altura (número de pixels por coluna)
- **Raios (amostras) por pixel:** quantidade de raios luminosos gerados por pixel da imagem. Para cada pixel serão gerados raios luminosos aleatórios dentro da região daquele pixel.
- **Profundidade máxima:** a profundidade máxima que a recursão de raios luminosos pode chegar. Essa recursão é gerada a partir da reflexão dos objetos, que pode gerar um novo raio luminoso, este podendo bater em um objeto e refletir novamente, e assim por diante.

As configurações usadas foram as seguintes:

- **test** (COLOCAR LINK DO YOUTUBE)
  - **Largura:** 100
  - **Altura:** 56
  - **Raios (amostras) por pixel:** 1
  - **Profundidade máxima:** 5
- **very-very-low** (COLOCAR LINK DO YOUTUBE)
  - **Largura:** 100
  - **Altura:** 56
  - **Raios (amostras) por pixel:** 5
  - **Profundidade máxima:** 10
- **very-low** (COLOCAR LINK DO YOUTUBE)
  - **Largura:** 200
  - **Altura:** 112
  - **Raios (amostras) por pixel:** 5
  - **Profundidade máxima:** 10
- **low** (COLOCAR LINK DO YOUTUBE)
  - **Largura:** 200
  - **Altura:** 112
  - **Raios (amostras) por pixel:** 10
  - **Profundidade máxima:** 10
- **medium-low** (COLOCAR LINK DO YOUTUBE)
  - **Largura:** 200
  - **Altura:** 112
  - **Raios (amostras) por pixel:** 50
  - **Profundidade máxima:** 20
- **medium-low+** (COLOCAR LINK DO YOUTUBE)
  - **Largura:** 400
  - **Altura:** 225
  - **Raios (amostras) por pixel:** 50
  - **Profundidade máxima:** 20
- **medium** (COLOCAR LINK DO YOUTUBE)
  - **Largura:** 400
  - **Altura:** 225
  - **Raios (amostras) por pixel:** 100
  - **Profundidade máxima:** 50

O vídeo final com todas as animações comparadas também está disponível no YouTube **COLOCAR LINK DO YOUTUBE**

## Atendimento dos requisitos

- [ ] **O projeto deve gerar uma animação com pelo menos 5 segundos:** a animação final pode ser acessada no YouTube **COLOCAR LINK DO YOUTUBE**
- [x] **a geração das imagens deve utilizar as implementações dos membros do grupo:** a implementação vem das atividades de um dos membros do grupo
- [x] **Utilize pelo menos 3 objetos sendo pelo menos um deles formado por triângulos:** foram usados um cubo e três esferas (totalizando quatro objetos). O cubo é um objeto formado por triângulos (cada face do cubo é formada por dois triângulos)
- [x] **Utilize materiais difusos e reflexivos:** as três esferas utilizam materiais difusos e o cubo utiliza material reflexivo (metálico)
- [x] **Faça pelo menos um movimento com a câmera e outro com pelo menos um dos objetos:** duas esferas rotacionam ao redor do cubo e a câmera também rotaciona ao redor do cubo

## Detalhes sobre a implementação

### Documentação online

A documentação do código criado pode ser [acessado online](https://gregoriofornetti.github.io/projeto-cg/docs/_build/html/index.html)

### Principais bibliotecas utilizadas no projeto

- [NumPy](https://numpy.org/): fornece estruturas de dados (arrays) e operações sobre elas que serão úteis para manipular e gerar as imagens.
- [Pillow](https://pypi.org/project/Pillow/): para salvar e ler imagens em diversos formatos.
- [Sphinx](https://www.sphinx-doc.org/pt_BR/master/): gerador de documentação a partir dos comentários de documentação incluídos no próprio código.
- [tqdm](https://tqdm.github.io/): para indicar progresso das operações/funções mais demoradas.
- [opencv](https://opencv.org/): para gerar o vídeo da animação a partir dos frames

### Instalação

Para conseguir executar o projeto, é necessário ter instalado o Python e todas as bibliotecas citadas. Para instalar mais facilmente as bibliotecas necessárias, foi criado o arquivo `requirements.txt`, e utilizando o pip (sistema de gerenciamento de pacotes do Python), é possível instalar todas as bibliotecas usando o comando `pip install -r requirements.txt`

### Mais informações

Detalhes a respeito do código podem ser consultados no README.md da pasta src. **COLOCAR LINK**


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
