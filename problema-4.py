from typing import NoReturn, List, Dict

"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP  R$67.836,43
RJ  R$36.678,66
MG  R$29.229,88
ES  R$27.165,48
Outros  R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do
valor total mensal da distribuidora.
"""


def main() -> NoReturn:
    invoice: List[Dict] = [
        {
            "SP": 67836.43,
            "RJ": 36678.66,
            "MG": 29229.88,
            "ES": 27165.48,
            "Outros Estados": 19849.53,
        }
    ]
    state_billing: list = []
    state_name: list = []
    percentual: list = []
    for state, value in invoice[0].items():
        state_billing.append(value)
        state_name.append(state)

    state_billing_sum = sum(state_billing)

    for value in state_billing:
        value = value * 100
        value = value / state_billing_sum
        percentual.append(value)

    response = zip(state_name, percentual)
    print("Resultado")
    for state, value in dict(response).items():
        print(
            f"{state} teve participação de {round(value, 2)}% dentro do valor total mensal da distribuidora."
        )


if __name__ == "__main__":
    main()
