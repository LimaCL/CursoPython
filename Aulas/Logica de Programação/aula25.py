# Interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço total foi R$ %.2f' % (nome, preco) # Luiz, o preço total foi R$ 1000.96
print(variavel)
print('O hexadecimmal de %d é %X' % (15, 15)) # O hexadecimmal de 15 é F
print('O hexadecimmal de %d é %04X' % (15, 15)) # O hexadecimmal de 15 é 000F
