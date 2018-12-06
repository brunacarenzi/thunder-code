#Adivinhando números

from random  import randint
pc = randint(0, 10)
print('Olá, estou pensando em um número entre 0 e 10...')
print('Será que você consegue adivinhar? Vamos lá!')
acertou = False
palpites = 0
#por enquanto o jogador não tentou
while not acertou:
    jogador = int(input('Digite seu palpite: '))
    palpites += 1  #acrescenta palpites até acertar
    if jogador == pc:
       acertou = True
    else:
        if jogador < pc:
            print('Mais...tente de novo!')
        elif jogador > pc:
            print('Menos... tente de novo!')
print('Acertou com {} tentativas. PARABÉNS!!'.format(palpites))
sair = str(input('Deseja sair do jogo?'))
if sair == 'sim':
    print('Ok, byeeee!!')
else:
    print('comece outra vez!')
















