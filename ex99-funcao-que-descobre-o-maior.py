# Ex 99 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros
# Seu programa tem que analisar todos os valores e dizer quel deles é o maior.
from time import sleep

def maior(* num):
    contador = 0
    maior = 0
    print('Analisando os valores informados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()