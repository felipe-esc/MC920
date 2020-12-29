# Lab 2 - aplicação de máscaras de difusão de erros
O código realiza a aplicação de máscaras em imagens em preto e branco com 6 máscaras definidas em `kernels.py`. As máscaras estão definidas em `masks.py`.

## Execução do código
O script foi executado usando-se `Python 3.8.5`, usando-se as bibliotecas `NumPy` e `OpenCV2`, executando-se o arquivo principal `lab02.py`pelo interpretador, como no exemplo:

`python lab02.py --input-file=input.png --output-file=output.png --mask=burkes --alternate`

E os argumentos possíveis são:

- input-file - caminho para a imagem png de entrada.
- output-file - caminho da imagem de saída pretendido.
- mask - mascára a ser aplicada dentre as disponíveis ('floyd-steinberg', 'stevenson-arce', 'burkes', 'sierra', 'stuckis' e 'jarvis-judice-ninke').
- alternate - opção para aplicação das máscaras alternando a orientação da aplicação entre uma linha e outra. (opcional)
- gray - opção para salvar a imagem em preto e branco. (opcional)

como também a primeira letra de cada um dos parâmetros é aceita, por exemplo:

`python lab02.py -i input.png -o output.png -m sierra -g`

Link para os [Requerimentos do trabalho](https://www.ic.unicamp.br/~helio/disciplinas/MC920/trabalho2.pdf)