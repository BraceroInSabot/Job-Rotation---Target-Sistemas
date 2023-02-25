"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no
código;

b) Evite usar funções prontas, como, por exemplo, reverse;
"""


def main(user_input: str) -> str:
    """
    Inverte os carcteres de um input
    """

    return print(user_input[::-1])


if __name__ == "__main__":
    insert: str = str(input("Escreva algo para inverter: \n"))
    main(user_input=insert)
