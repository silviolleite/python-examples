"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o
programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos
duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um
valor "A" para A.M. e "P" para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal
para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos
valores de entrada todas as vezes que desejar.

- [x] Converter 14:25 para 2:25 P.M.
- [x] Ler dois inteiros
- [x] Ter duas funções uma para conversão e outra para a saída
- [x] Registrar A.M./P.M. com valor "A" para A.M. e "P" para P.M.
- [x] Ter um loop que permita que o usuário repita esse cálculo para novos
valores de entrada todas as vezes que desejar
"""

# Constante com o mapa dos períodos
PERIODS = {
    "A": "A.M.",
    "P": "P.M."
}


def show_hour(hour, minute, period):
    """
    Mostra a hora formatada

    :param hour: int
    :param minute: int
    :param period: string
    :return: void

    >>> show_hour(12, 15, "A")
    12:15 A.M.
    >>> show_hour(1, 15, "P")
    1:15 P.M.
    """
    print(f"{hour}:{minute} {PERIODS[period]}")


def converter_hour(hour):
    """
    Converter horas no formato 24 horas para o formato 12 horas

    :param hour: int
    :return: int, string

    >>> converter_hour(12)
    (12, 'A')
    >>> converter_hour(13)
    (1, 'P')
    """
    if hour <= 12:
        return hour, "A"
    else:
        return hour - 12, "P"


if __name__ == "__main__":
    while True:
        # Solicita as horas
        while True:
            input_hour = int(input("Hora no formato 24hs: "))
            if 0 < input_hour < 24:
                break
            print("Hora inválida!")

        # Solicita os minutos
        while True:
            input_minute = int(input("Minutos: "))
            if 0 < input_minute < 60:
                break
            print("Minutos inválido!")

        new_hour, period_key = converter_hour(input_hour)
        show_hour(new_hour, input_minute, period_key)

        # controle de fluxo
        want_continue = input("Gostaria de continuar [s,n]: ")
        if want_continue.lower() == "n":
            print("Finalizado!")
            break

        print(20 * "*")
        print("Nova conversão de horas")
        print(20 * "*")
        print()
