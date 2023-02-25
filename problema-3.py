from random import uniform
from time import sleep
import requests
import json
import datetime

"""
Simluação do faturamento mensal de uma empresa representada por 5 semanas
"""


def create_json():
    """
    Cria um arquivo JSON para simular a data dos rendimentos da empresa.
    """
    day: dict = {}

    feb_start = datetime.date(2023, 2, 1)
    feb_end = datetime.date(2023, 2, 28)

    def month_simulation(day: dict = day):
        """
        Cria uma lista de decimais com valores aleatórios entre 50 e 100.
        """
        holidays = []

        request = requests.get("https://brasilapi.com.br/api/feriados/v1/2023")

        ctx = json.loads(request.content)
        for x in range(0, len(ctx)):
            api_date = ctx[x]["date"]
            holidays.append(api_date)

        for x in range(1, feb_end.day - feb_start.day + 2):
            week_d = datetime.date(2023, 2, x).weekday()

            a = round(uniform(50, 100), 2)

            if week_d == 5 or week_d == 6:
                day[f"day {x}"] = False
                continue
            elif str(datetime.date(2023, 2, x)) in holidays:
                day[f"day {x}"] = False
                continue
            else:
                day[f"day {x}"] = a

        return day

    month_simulation()

    day_dump = json.dumps(day)
    day_loads = json.loads(day_dump)

    with open("problema-3.json", "w") as file:
        json.dump(day_loads, file)
        file.close()

    return print("Arquivo JSON criado com sucesso!")


def data_unpacking():
    """
    Desempacota arquivo JSON feito.
    """
    data_values = []

    with open("problema-3.json", encoding="utf-8") as file:
        json_data = json.load(file)

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

    def data_processing(data=data_values):
        """
        Processa os dados e entrega as respostas das questões
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
        return True

    return data_processing()


if __name__ == "__main__":
    create_json()

    for time in range(3):
        sleep(1)
        print("...")

    data_unpacking()