# Lab 4 - Esteganografia
O código implementa a função de esconder e reaver mensagens secretas em imagens, pelo meio da técnica de esteganografia.

## Execução do código
O script foi executado usando-se `Python 3.8.5`, usando-se as bibliotecas `NumPy` e `OpenCV2`, executando-se o arquivo principal `lab04.py`pelo interpretador, como no exemplo:

`python lab04.py --input-file=input.png --output-file=output.png --text=sample.txt --code --bit-plan=1 --separate`
ou 
`python lab04.py --input-file=input.png --text=sample.txt --decode --bit-plan=1`

E os argumentos possíveis são:

- input-file - caminho para a imagem png de entrada.
- output-file - caminho da imagem de saída pretendida caso se escolha codificar uma mensagem. Não é usado para decodificação.
- text - caminho para o arquivo de texto plano que se queira ler/escrever ou texto digitado a ser inserido. Pode ser omitido caso queira-se decodificar.
- bit-plan - plano de bit a ser codificado ou decodificado.
- code/decode - opção para inserir ou extrair mensagem de texto.
- separate - opção para separar os canais 0, 1, 2 e 7 na codificação. (opcional)

como também a primeira letra de cada um dos parâmetros é aceita, por exemplo:

`python lab04.py -i input.png -o output.png -t sample.txt -c -b 1 -s`
ou 
`python lab04.py -i input.png -t sample.txt -d -b 1`


Link para os [Requerimentos do trabalho](https://www.ic.unicamp.br/~helio/disciplinas/MC920/trabalho4.pdf)