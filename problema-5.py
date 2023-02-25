def main(user_input: str) -> str:
    """
    Inverte os carcteres de um input
    """

    return print(user_input[::-1])


if __name__ == "__main__":
    insert = str(input("Escreva algo para inverter: \n"))
    main(user_input=insert)
