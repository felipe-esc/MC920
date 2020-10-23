# Lab 1 - aplicação de Kernels
O código realiza a convolução com 11 kernels definidos em `kernels.py` usando OpenCV, facilmente editáveis para que se realize com qualquer outro desejado com um pouco de edição.

## Execução do código
O script foi executado usando-se `Python 3.8.5`, usando-se as bibliotecas `NumPy` e `OpenCV2`, executando-se o arquivo principal `lab01.py`pelo interpretador, como no exemplo:

`python lab01.py -i input.png -o output.png --kernel 8`

E os argumentos possíveis são:

- input - caminho para a imagem \verb|png| de entrada.
- output - caminho da imagem de saída pretendido.
- kernel - kernel pretedido entre os 11 disponíveis.
- combine - opção para usar a combinação entre os kernels 3 e 4.

como também a primeira letra de cada um dos parâmetros é aceita, por exemplo:

`python lab01.py -i input.png -o output.png -k 7`
