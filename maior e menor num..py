# mostrar qual valor é o maior e qual e o menor
print('Olá, por favor teste este esse programa.')
n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número:'))
n3 = int(input('Informe o 3º número:'))

# Verificando o menor número
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando o maior número
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor número é:{}'.format(menor))
print('O maior número é: {}'.format(maior))
print(f'Multiplicação entre maior e menor número: {maior} * {menor} = {maior * menor}')
print(f'Soma entre maior e menor número: {maior} + {menor} = {maior + menor}' )