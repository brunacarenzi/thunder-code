# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

nome = str(input('Olá, digite seu nome:')).strip().upper()
salario = float(input('Agora, digite seu salário: R$'))
aumento = (1.15 * salario)
print('Seu salário de R${:.3f} passa a ser R${:.3f} devido ao aumento de 15%.'.format(salario,aumento))
