# INTRODUÇÃO A FORMATAÇÃO DE STRINGS

nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura' #.2f (Duas casas decimais)
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

 
print(linha_1) # Luiz Otávio tem 1.80 de altura
print(linha_2) # pesa 95 quilos e seu IMC é
print(linha_3) # 29.32