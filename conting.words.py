a = str(input('Digite alguma frase: ')).strip().upper()
b = str(input('Digite outra frase: ')).strip().upper()
print(f'+ A 1ª frase contém {len(a)} caracteres.')
print(f'+ A 2ª frase contém {len(b)} caracteres.')
if a != b:
    print('* A quantidade de caracteres é desigual.')
else:
    print('* A quantidade de caracteres são iguais.')