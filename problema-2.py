"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores

(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 

ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""


def fibonacci(x: int) -> str:
    """
    Recebe uma variavel com um inteiro e renderiza de fundo uma sequência de Fibonacci. No seu retorno, avisa o usuário
    se o número está presente ou não na sequência.
    """
    p1 = 1
    p2 = 1

    while True:
        response = p2 + p1
        p1 = p2
        p2 = response

        if x == p1:
            return print("O número informado pertence a sequência!")
        elif x < p1:
            return print("O número informado não pertence a sequência.")


if __name__ == "__main__":
    try:
        numb = int(input("Que termo deseja encontrar: "))
    except ValueError as err:
        print(f"Houve um erro ao receber a informação. \n--{err}")

    fibonacci(numb)
