#Atividade bancária sem o uso de classes

def lin():
    print('-' * 30)
def depositar():
    print('Depósito em conta')
def imprimir():
    print(f' + Conta:{dados}')
    print(f' + CPF:{cpf}')
    print(f' + {nome}')
    if dep == 'N':
        print(f'+ Seu saldo é devedor de R$-{saque}')
    else:
        print(f'+ Saldo de R${deposito}')




lin()
print('         BANCO UAM       ')
lin()
print('Saldo inicial:R$0,00')
print('Limite de saques cont. especial: R$500,00')
dados = float(input('Número da conta: '))
cpf = int(input('CPF: '))
nome = str(input('Digite seu nome: ')).upper()
print(f' Olá,{nome}! Seja bem-vindo(a)!')

limite = 500
lin()
saque = float(input('Digite um valor para saque: R$ '))
while True:

    if saque > limite:
        print(' * Você Não pode ultrapassar o limite de R$500,00')
        saque2 = float(input('Digite outro valor válido: R$ '))
        print(f'Você sacou: R$ {saque2} reais.')
    elif saque <= limite:
        print(f'Saque de R${saque} reais aprovado!')
        print('Retire suas notas!')

    break


lin()
dep = str(input('Deseja fazer deposito? S/N   ')).strip().upper()
if dep == 'S':
    depositar()
    deposito = float(input('Digite o valor do depósito: R$ '))
    print(f'O valor de R$ {deposito} será depositado em até 1 dia útel.')
    lin()
elif dep == 'N':
    print(' Ação canselada!')


lin()
imprimir()



