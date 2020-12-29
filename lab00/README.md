# Trabalho 0 - Opcional [Não entregue]
Trabalho opcional, apenas para familiarização com as bibliotecas a serem usadas no semestre. 
[Requerimentos do trabalho](https://www.ic.unicamp.br/~helio/disciplinas/MC920/trabalho0.pdf)

Os scripts foram executados usando-se `Python 3.8.5`, usando-se as bibliotecas `NumPy` e `OpenCV2`.

## Instruções:

### 1.1
Implementa diversas funções simples em imagens.

Exemplo de comando:
`python lab00_1-1.py -i input.png -o output.png -f negative`

Argumentos aceitos (como também a primeira letra de cada um dos parâmetros é aceita):
- input-file - caminho para a imagem png de entrada.
- output-file - caminho da imagem de saída pretendido.
- function - nome da função a ser executada dentre: "negative", "mirror", "range", "invert" e "reflect".

### 1.2
Implementa ajuste de brilho em imagens.

Exemplo de comando:
`python lab00_1-2.py -i input.png -o output.png -g 0.5`

Argumentos aceitos (como também a primeira letra de cada um dos parâmetros é aceita):
- input-file - caminho para a imagem png de entrada.
- output-file - caminho da imagem de saída pretendido.
- gamma - argumento gamma para a função de ajuste de brilho.

### 1.3
Implementa extração de plano de bits de uma imagem.

Exemplo de comando:
`python lab00_1-3.py -i input.png -o output.png -b 3`

Argumentos aceitos (como também a primeira letra de cada um dos parâmetros é aceita):
- input-file - caminho para a imagem png de entrada.
- output-file - caminho da imagem de saída pretendido.
- bit - plano de bit a ser extraído. [bits devem ser de 0 a 7]

### 1.4
Implementa um script que pega uma imagem e cria um mosaico aleatório com ela.

Exemplo de comando:
`python lab00_1-4.py -i input.png -o output.png`

Argumentos aceitos (como também a primeira letra de cada um dos parâmetros é aceita):
- input-file - caminho para a imagem png de entrada.
- output-file - caminho da imagem de saída pretendido.

### 1.5
Implementa a fusão de duas imagens, dado um peso para a primeira imagem.

Exemplo de comando (como também a primeira letra de cada um dos parâmetros é aceita):
`python lab00_1-5.py -f input1.png -s input2.png -o output.png -w 0.6`

Argumentos aceitos:
- first-image - caminho para a primeira imagem png de entrada.
- second-image - caminho para a segunda imagem png de entrada.
- output-file - caminho da imagem de saída pretendido.
- weight - peso para a primeira imagem dentre (0, 1).
