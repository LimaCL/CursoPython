# Introdução ao try/except
# try -> tente executar o código
# except -> ocorreu algum erro ao tentar executar

numero = input('Vou dobrar o número que você digitar: ')

# if numero.isdigit():
#    numero_float = float(numero)
#    print(f'O dobro de  {numero} é {numero_float * 2}')
# else:
#    print('Isso não é um numero')

try:
    numero_float = float(numero)
    print('FLOAT: ', numero_float)
    print(f'O dobro de  {numero} é {numero_float * 2}')
except:
    print('Isso não é um numero')