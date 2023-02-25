def main():
    invoice = [
        {
            "SP": 67836.43,
            "RJ": 36678.66,
            "MG": 29229.88,
            "ES": 27165.48,
            "Outros Estados": 19849.53,
        }
    ]
    state_billing = []
    state_name = []
    percentual = []
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

    return True


if __name__ == "__main__":
    main()
