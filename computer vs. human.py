#Criando interação entre computador e usuário

print('-=' * 10)
print(' \033[7;30;0m Pc conhece humano \033[m')
print('-=' * 10)
print('Bem-vindo! Vamos nos conhecer =D!\n')
nome = str(input('Olá, qual é o seu nome? \n ')).strip().capitalize()
len(nome)
print('Seu nome tem {} letras =)!'.format(len(nome)))
cores = {'limpa': '\033[m',
         'verde': '\033[32m',
         'roxo': '\033[35m',
         'verdeagua': '\033[36m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebrando': '\033[7;30m'}
if nome == 'Bruna':
    print('{}{}{} que lindo nome!'.format(cores['verdeagua'], nome, cores['limpa']))
    print('Ah, e meu nome é PC028, mas pode me chamar de PC, muito prazer!')
else:
    print('{}{}{} que nome bonito! Mas acho o meu nome mais legal u.u!'.format(cores['roxo'], nome, cores['limpa']))
    print('Ah, e meu nome é PC028, mas pode me chamar de PC mesmo, muito prazer!')

idade = int(input('Agora, please me fale sua idade:\n '))
if idade >= 18:
    print(' Caramba,você está com {}{}{} anos, já é\033[1;33;0m uma pessoa adulta\033[m O.O!'.format(cores['verde'],
                                                                                                     idade,
                                                                                                     cores['limpa']))
else:
    print(' Você está com {}{}{} anos, você ainda não é \033[1;33;0m ADULTO \033[m u.u...'.format(cores['roxo'], idade,
                                                                                                  cores['limpa']))
    print('Agora que sei seu nome e sua idade, preciso saber agora onde você mora?')

end = str(input('Digite seu endereço aqui: \n')).strip().title()

print('Hum, legal!! Então, você mora em {}{}{}...'.format(cores['azul'], end, cores['limpa']))
print('Já eu, vivo aqui sozinho mas eu gosto dessa ''vida'' de lobo solitário u.u\n')
from random import randint
#Jogo da adivinhação com números

pc = randint(0, 10)
print('*' * 65)
print('                      GAAAAAAME TIIIIIIME !!!                         ')
print('*' * 65)
print('Acabei de pensar em um número entre 0 á 10 [OuO]')
print('Preciso que me dê palpites, {}\n'.format(nome))
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais...tente mais uma vez\n')
        elif jogador > pc:
            print('Menos...tente mais uma vez\n')
print('Acertou com {} tentativas, Parabéns!!!'.format(palpites))

print('*' * 65)
print('Gostaria de continuar com os jogos? ')

while True:
    keep = str(input('Digite [S] ou [N] para escolher:')).strip().upper()
    if keep == 'S':
        print('Sua resposta foi SIM, então vamos continuar!!')
    elif keep == 'N':
        print(' Saindo do jogo...')
        break

 #Jogo de Jopenpo

from random import randint
from time import sleep
lista = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('X X X JOKENPO X X X')
perguntar = int(input('''Escolha uma opção para jogar:
[0] Pedra
[1] Papel
[2] Tesoura  
Digite sua escolha: '''))

print('JO\n')
sleep(1)
print('KEN\n')
sleep(1)
print('POOH!!\n')
print('#' * 20)
print('O computador escolheu: {}'.format(lista[computador]))
print('O jogador escolheu {}'.format(lista[perguntar]))
print('#' * 20)
if computador == 0:
    if perguntar == 0:
        print('EMPATE!')
    elif perguntar == 1:
        print('JOGADOR PERDEU!')
    elif perguntar == 2:
        print('PC VENCEU!')
    else:
        print('OPERAÇÃO INVÁLIDA!')
elif computador == 1:
    if perguntar == 0:
        print('PC PERDEU!')
    elif perguntar == 1:
        print('EMPATE!')
    elif perguntar == 2:
        print('JOGADOR VENCEU!')
    else:
        print('OPERAÇÃO INVÁLIDA!')
elif computador == 2:
    if perguntar == 0:
        print("Jogador venceu")
    elif perguntar == 1:
        print("Computador venceu")
    elif perguntar == 2:
        print("Empate!")
    else:
        print("Operacao invalida")
else:
    print('FIM DE JOGO')
print(' Estou cansadx...acho que vou dormir >o<')
print(' Até mais tarde!')
