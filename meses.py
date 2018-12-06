'''Escreva o método chamado getMesPorExtenso() que recebe um inteiro,
referente ao mês do ano, um código referente ao idioma (1 para português e 2
para inglês) e retorne o mês por extenso. A tabela a seguir ilustra alguns exemplos.'''

#meses em Português

mesesp = ('zero', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
         'Setembro', 'Outubro', 'Novembro', 'Dezembro')

#meses em Inglês
mesesi = ('zero', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', ' October', 'November', 'December')


while True:
    numero = int(input('*Digite um número entre 1 e 12 que te direi qual é o mês: '))
    if 0 <= numero <= 12:
        break
    print('Tente novamente', end='')
op = int(input('* Digite 1 para português ou 2 para ingles: '))
if op == 1:
    print(f'* Você digitou opção 1 [português]: o mês é {mesesp[numero]}')
elif op == 2:
    print(f'* Você digitou opção 2 [inglês]: the month is {mesesi[numero]}')

