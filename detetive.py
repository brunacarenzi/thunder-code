print('Por favor, responda as questões abaixo:')
a = str(input('Telefonou para a vítima antes do crime?'))
b = str(input('Esteve no local do crime?'))
c = str(input('Mora perto da vítima?'))
d = str(input('Devia dinheiro pra vitima?'))
e = str(input('Já brigou com a vitima?'))
if (a == b):
    print('Você é suspeito!')
if not (a == b):
    print('Ainda não é culpado...Vamos examinar as outras respostas')
elif (c == d != e):
    print('Você é cumplice de assassinato!')
elif not (c == d != e):
    print('Não é cumplice...')
else:
    print('Vamos estudar o caso!')


