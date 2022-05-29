"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o
programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos
duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um
valor "A" para A.M. e "P" para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal
para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos
valores de entrada todas as vezes que desejar.

- [X] Converter 14:25 para 2:25 P.M.
- [x] Ler dois inteiros
- [X] Ter duas funções uma para conversão e outra para a saída
- [x] Registrar A.M./P.M. com valor "A" para A.M. e "P" para P.M.
- [x] Ter um loop que permita que o usuário repita esse cálculo para novos
valores de entrada todas as vezes que desejar
"""


KEY_A = "A"
KEY_P = "P"
PERIODS = {
    KEY_A: "A.M.",
    KEY_P: "P.M."
}


def converter_hour(hour):
    """
    Converter horas do formato 24 para o 12

    :param hour: int
    :return: int, string

    >>> converter_hour(12)
    (12, 'P')
    >>> converter_hour(0)
    (12, 'A')
    >>> converter_hour(13)
    (1, 'P')
    >>> converter_hour(7)
    (7, 'A')
    >>> converter_hour(17)
    (5, 'P')
    >>> converter_hour(23)
    (11, 'P')
    >>> converter_hour(11)
    (11, 'A')
    """
    if hour == 0:
        return 12, KEY_A
    elif hour < 12:
        return hour, KEY_A
    elif hour == 12:
        return hour, KEY_P
    else:
        return hour - 12, KEY_P


def show_hour(hour, minute, period):
    """
    Mostra a data formatada

    :param hour: int
    :param minute: int
    :param period: string
    :return: void

    >>> show_hour(12, 15, "A")
    12:15 A.M.
    >>> show_hour(11, 25, "P")
    11:25 P.M.
    >>> show_hour(1, 15, "A")
    01:15 A.M.
    >>> show_hour(1, 15, "P")
    01:15 P.M.
    >>> show_hour(1, 1, "P")
    01:01 P.M.
    >>> show_hour(1, 1, "A")
    01:01 A.M.
    """
    print(f'{hour:0>2}:{minute:0>2} {PERIODS[period]}')


def validate_hour(hour):
    """
    Valida a hora no formato 24 horas

    :param hour: int
    :return: bool

    >>> validate_hour(24)
    False
    >>> validate_hour(0)
    True
    >>> validate_hour(17)
    True
    >>> validate_hour(25)
    False
    >>> validate_hour(-1)
    False
    """
    return 0 <= hour < 24


def validate_minute(minute):
    """
    Valida os minutos

    :param minute: int
    :return: bool

    >>> validate_minute(-1)
    False
    >>> validate_minute(0)
    True
    >>> validate_minute(60)
    False
    >>> validate_minute(25)
    True
    >>> validate_minute(59)
    True
    >>> validate_minute(61)
    False
    """
    return 0 <= minute < 60


if __name__ == '__main__':
    while True:
        # Solicita a hora
        while True:
            input_hour = int(input("Hora no formato 24 hrs: "))
            if validate_hour(input_hour):
                break
            print("Hora inválida!")

        # Solicita os minutos
        while True:
            input_minute = int(input("Minutos: "))
            if validate_minute(input_minute):
                break
            print("Minuto inválido!")

        # Convertendo a hora
        new_hour, period = converter_hour(input_hour)

        # Exibe a hora formatada
        show_hour(new_hour, input_minute, period)

        # Verificação se o usuário quer continuar
        want_continue = input("Gostaria de continuar [s,n]: ")
        if want_continue.lower() == "n":
            print("Finalizado!")
            break

        print(20 * "*")
        print("Nova conversão de horas")
        print(20 * "*")
        print()
