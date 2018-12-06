c = int
n1 = int(input('Digite o 1º número:'))
n2 = int(input('Digite o 2º número: '))
print('''Escolha a função que deseja calcular
[1]SOMAR
[2]MULTIPLICAR
[3]MAIOR
[4]TROCAR DE NÚMEROS
[5]SAIR DO PROGRAMA
 ''')
op = int(input('Qual é a opção? '))
if op == 1:
    c = n1 + n2
    print(f'A opção escolhida foi 1 de soma: {n1} + {n2} = {c}')
elif op == 2:
    c = n1 * n2
    print(f'A opção escolhida foi 2 de multiplicação: {n1} * {n2} = {c}')
elif op == 3:
    c = n1 > n2 or n2 > n1
    if n1 == n2:
        print('Os números {} e {} são iguais!'.format(n1, n2))


elif op == 5:
    print('Sair!')

while op == 4:
    n3 = int(input('Informe outro número: '))
    n4 = int(input('Informe mais um número: '))
    op = int(input('informe a função: '))
    if op == 1:
        s = n3 + n4
        print('Função soma: {} + {} = {} '.format(n3, n4, s))
    elif op == 2:
        m = n3 * n4
        print('Função multiplicação: {} * {} = {}'.format(n3, n4, m))

    break




