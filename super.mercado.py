# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
print('-------Super Mercado-------')
c = float(input('Código produto:'))
if c ==2335:
    print('carrinho de controle remoto')
elif c == 1234:
    print('boneca barbie')
elif c == 5554:
    print('ursinho')
else:
    print('Não há itens!')
    print('Por favor, informe o valor do produto a seguir.')

v = float(input('Digite o valor do produto:R$'))
d = (v * 0.05)
print('Desconto de 5% : R$ {:.2f}'.format(d))
print('Total a pagar: R$ {:.2f}'.format(v - d))
