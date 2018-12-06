def lin():
    print('-' * 30)




cadastro = []

while True:

    conta = float(input('Digite o número da conta para cadastro: '))
    cadastro.append(conta)


    op = str(input('Deseja cadastrar outra conta? S/N ')).strip().upper()
    if op == 'S':
        print('Cadastrando...')

        lin()

    elif op == 'N':
        print(f'+ As contas foram cadastradas com sucesso!')
        break

print(f'+ Total de contas cadastradas é de:{len(cadastro)} contas')
print(f'+ Contas cadastradas:\n {sorted(cadastro)}')












