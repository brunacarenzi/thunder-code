'''Cadastro'''

print('+' * 20)
print(' FICHA DE CADASTRO ')
print('+' * 20)
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        tot18 += 1
        print('Maior de idade!')
        print('+' * 20)

    elif idade < 17:
        print('Menor de idade!')
        print('+' * 20)
    sexo = str(input('Digite seu sexo: ')).strip().upper()
    if sexo == 'M':
        totH += 1
        print('Sexo masculino 0->')
        print('+' * 20)
    elif sexo == 'F' and idade < 20:
        totM20 += 1
        print('Sexo feminino 0-+')
        print('+' * 20)


    print('  Quer continuar?  ')
    continuar = str(input('Digite [S] ou [N] para proseguirmos: ')).strip().upper()
    if continuar == 'N':
        print(f'Há {tot18} pessoas maior de idade')
        print(f'Há {totH} Homens cadastrados')
        print(f'Há {totM20} Mulheres menos de 30 anos')
        print('+' * 20)
        print(' - Fim da execução -')
        break
    elif continuar == 'S':
        print('Vamos continuar...')


