from random import randint
numero = int(input('Digite um número para saber se é par ou impar:'))
resto = numero % 2

if resto == 0:
    print('Número {} é par'.format(numero))
else:
    print(f'Número {numero} é impar')
pc = randint(0, 10)
resto = numero % 2
print(' escolhi {}'.format(pc))


