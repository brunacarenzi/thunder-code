'''2 – Criar o método converterHoras() que recebe um valor em segundos como
parâmetro, faça a conversão desse valor para horas, minutos e segundos e
imprima o resultado.'''

entrada = int(input('Informe os segundos que deseja converter: '))
a = entrada % 60

tempo_m = entrada % 60

b = tempo_m % 60

c = tempo_m % 60

print( c, 'horas', b, 'minutos e', a, 'segundos')