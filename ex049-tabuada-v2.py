# 49 Tabuada v.2.0  Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

num = int(input('Digite um número interio para ver a sua tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')


