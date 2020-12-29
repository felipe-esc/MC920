# Lab 3 - Separação de fundos por meio de funções de limiares
O código implementa diversas funções de separação de objetos e fundos aplicando funções simples em relação à imagem global ou à vizinhança.

## Execução do código
O script foi executado usando-se `Python 3.8.5`, usando-se as bibliotecas `NumPy` e `OpenCV2`, executando-se o arquivo principal `lab03.py`pelo interpretador, como no exemplo:

`python lab03.py --input-file=input.png --output-file=output.png --histogram`

E os argumentos possíveis são:

- input-file - caminho para a imagem png de entrada.
- output-file - caminho da imagem de saída pretendido.
- histogram - opção para gerar um histograma de distribuição de tons da imagem final. (opcional)

como também a primeira letra de cada um dos parâmetros é aceita, por exemplo:

`python lab03.py -i input.png -o output.png`

As funções e parâmetros são pedidos conforme a execução do programa.

## Funções e parâmetros:
### Global
- Thresold - limiar para separação de objetos.

### Bernsen
Nenhum parâmetro é requerido.

### Niblack
- k - parâmetro k.

### Sauvola-Pietaksinen
- k - parâmetro k.
- R - parâmetro R.

### Phansalskar-More-Sabale
- k - parâmetro k.
- R - parâmetro R.
- p - parâmetro q.
- q - parâmetro q.

### Contrast
Nenhum parâmetro é requerido.

### Mean
Nenhum parâmetro é requerido.

### Median
Nenhum parâmetro é requerido.

Para mais infos sobre as funções acesse o link para os [Requerimentos do trabalho](https://www.ic.unicamp.br/~helio/disciplinas/MC920/trabalho3.pdf)