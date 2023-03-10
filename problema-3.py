from typing import NoReturn
from json import load
from locale import setlocale, currency, LC_ALL


def data_unpacking():
    """
    Desempacota e lê arquivo JSON criado pelo algoritmo.
    """
    data_values = []

    with open("dados.json", encoding="utf-8") as file:
        json_data = load(file)

    for key in json_data:
        [data_values.append(key["valor"]) if key["valor"] else False]

    def data_processing(data: list = data_values) -> NoReturn:
        """
        Processa os dados para ser entregue as respostas das questões.
        """

        # Primeira questão
        setlocale(LC_ALL, "")
        print(
            f"O menor valor de faturamento ocorrido em um dia do mês: {str(currency(round(min(data), 2), grouping=True))}"
        )
        # Segunda questão
        print(
            f"O maior valor de faturamento ocorrido em um dia do mês: R${str(currency(round(max(data), 2), grouping=True))}"
        )

        # Terceira e última questão
        mean = lambda x: sum(x) / len(x)
        mean = round(mean(data), 2)
        # print(mean)
        i = 0
        for x in data:
            if mean < x:
                i += 1

        print(
            f"\nNúmero de dias no mês em que o valor de faturamento diário foi superior à média mensal: {i}"
        )

    return data_processing()


if __name__ == "__main__":
    data_unpacking()
