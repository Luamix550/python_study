#!/usr/bin/env python3
from random import randint
from time import sleep

from random import randint
from time import sleep

def redondear_valor(valor):
    return round(valor, 2)

def realizar_pago_efectivo(valor_total):
    while True:
        pago = int(input(f"Total a pagar: ${valor_total}\nCon cuánto dinero paga -> "))
        if pago < valor_total:
            print(f"El monto es inválido, ha ingresado: ${pago}.\nDebe pagar: ${valor_total}\nSaldo faltante: ${redondear_valor(valor_total - pago)}\nVuelva a intentarlo.")
        else:
            cambio = redondear_valor(pago - valor_total)
            print(f"Cambio: ${cambio}\nRetire su cambio...")
            sleep(3)
            print("Gracias por visitarnos!")
            exit()

def realizar_pago_tarjeta_credito():
    print("Ingrese su tarjeta.")
    sleep(3)
    join_c_card_pwd = input("Ingrese su contraseña: ")
    if join_c_card_pwd == c_card_pwd:
        c_num = input("Numero de cuotas: ")
        if c_card_active:
            print("Pago aceptado.")
            sleep(2)
            print("Gracias por visitarnos!")
            exit()
        else:
            print("Pago rechazado.")
            sleep(2)
    else:
        print("La contraseña es incorrecta.")
        sleep(2)

def realizar_pago_tarjeta_debito(valor_total):
    print("Ingrese su tarjeta.")
    sleep(3)
    join_d_card_pwd = input("Ingrese su contraseña: ")
    if join_d_card_pwd == d_card_pwd:
        if d_card_sald < valor_total:
            for _ in range(2):
                print("Saldo insuficiente.\nReintentando pago...")
                sleep(2)
                if d_card_sald < valor_total:
                    print("Tarjeta rechazada.")
                else:
                    break
        elif d_card_sald >= valor_total:
            print("Pago aceptado.")
            sleep(2)
            print("Gracias por visitarnos!")
            exit()
    else:
        print("La contraseña es incorrecta.")

def pay_nequi():
            print("Elige si la transferecia sera por numero o QR:")
            sleep(2)
            nequi_transfer = input("\n|    1    ||      2     ||    3     |\n| Numero  ||      QR    ||   Atras  |")
            if nequi_transfer == "1" or nequi_transfer == "Numero":
                print(f"\nNumer nequi: {number_nequi}.\n")
                nequi_transfer = input("Ingresa el numero a realizar transferencia\n")
                if nequi_transfer == number_nequi:
                    if sald_nequi > value_aux:
                        print("Transferencia exitosa.")
                        sleep(2)
                        print("Gracias por visitarnos!")
                        exit()
                    else:
                        print("Saldo insuficiente\n")
                else:
                    print("Numero equivocado..\n")

if __name__ == "__main__":
    order = redondear_valor(randint(1, 3000))
    tips = redondear_valor((order * 10) / 100)
    valor_total = 0
    i = True
    d_card_sald = randint(1, 3000)
    d_card_pwd = "2206"
    c_card_pwd = "1234"
    c_card_active = bool(randint(0, 1))
    number_nequi = "312345678"
    sald_nequi = randint(1, 3000)

    while i:
        print(f"El total de su cuenta es: ${order}.\nDesea incluir la propina del 10%?\nCuenta: ${redondear_valor(order + tips)}\n   |si = 1|   |no = 2|\n")
        us_r = input()
        if us_r in ["si", "1"]:
            value_aux = redondear_valor(order + tips)
            i = False
        elif us_r in ["no", "2"]:
            value_aux = redondear_valor(order)
            i = False
        else:
            print(f"Ingrese una opción correcta.\n{'-' * 78}")
            sleep(2)

    while True:
        method = input(f"\nElija su método de pago:\n|   1  |   |   2  |   |   3    |\n| Cash |   | Card |   | Otro ->|\n\n{'-' * 78}\n")
        if method in ["1", "cash"]:
            realizar_pago_efectivo(value_aux)
        elif method in ["2", "card"]:
            card = input("|    1    ||    2   ||    3   |\n| Credito || Debito || Atrás  |\n")
            if card in ["1", "credito"]:
                realizar_pago_tarjeta_credito()
            elif card in ["2", "debito"]:
                realizar_pago_tarjeta_debito(valor_total)
            elif card in ["3", "atras"]:
                pass
        elif method in ["3", "otro"]:
            transfer = input("Elige tu metodo de pago:\n|    1   ||      2      ||    3   |\n| Nequi  || Bancolombia || Atrás  |\n")
            if transfer in ["1", "nequi"]:
                pay_nequi()
        else:
            print("Ingrese una opción correcta.\n")
            sleep(2)