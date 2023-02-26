from random import uniform
from time import sleep
from typing import NoReturn
from datetime import datetime, date
from requests import get
from json import load, loads, dump, dumps


"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que
desejar, que calcule e retorne:

• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:

a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;

b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo
da média;
"""


def create_json() -> str:
    """
    Cria um arquivo JSON para simular o valor e data dos rendimentos diários da empresa.
    """
    day: dict = {}

    feb_start: datetime = date(2023, 2, 1)
    feb_end: datetime = date(2023, 2, 28)

    def month_simulation(day: dict = day):
        """
        Cria uma lista de decimais com valores aleatórios entre 50 e 100 para serem usados como rendimentos.
        """
        holidays: list = []

        request = get("https://brasilapi.com.br/api/feriados/v1/2023")

        ctx = loads(request.content)
        for x in range(0, len(ctx)):
            api_date = ctx[x]["date"]
            holidays.append(api_date)

        for x in range(1, feb_end.day - feb_start.day + 2):
            week_d: int = date(2023, 2, x).weekday()

            a = round(uniform(50, 100), 2)

            if week_d == 5 or week_d == 6:
                day[f"day {x}"] = False
                continue
            elif str(date(2023, 2, x)) in holidays:
                day[f"day {x}"] = False
                continue
            else:
                day[f"day {x}"] = a

        return day

    month_simulation()

    day_dump = dumps(day)
    day_loads = loads(day_dump)

    with open("problema-3.json", "w") as file:
        dump(day_loads, file)
        file.close()

    return print("Arquivo JSON criado com sucesso!")


def data_unpacking() -> function:
    """
    Desempacota e lê arquivo JSON criado pelo algoritmo.
    """
    data_values = []

    with open("dados-alternativos.json", encoding="utf-8") as file:
        json_data = load(file)

    try:
        show_result = str(
            input("Você deseja ver o os números de rendimento da empresa? s/n")
        )
    except ValueError as err:
        print(err)

    for key, value in json_data.items():
        if show_result.lower() == "s":
            print(f'"{key}": {value},')

        if value:
            data_values.append(value)

    def data_processing(data: list = data_values) -> NoReturn:
        """
        Processa os dados para ser entregue as respostas das questões.
        """

        # Primeira questão
        print(
            f"O menor valor de faturamento ocorrido em um dia do mês: R${str(min(data)).replace('.', ',')}"
        )
        # Segunda questão
        print(
            f"O maior valor de faturamento ocorrido em um dia do mês: R${str(max(data)).replace('.', ',')}"
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
            f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {i}"
        )

    return data_processing()


if __name__ == "__main__":
    create_json()

    for time in range(3):
        sleep(1)
        print("...")

    data_unpacking()
