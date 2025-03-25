# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

#exemplo base
if senha == '123':
    print('Entrou')
else:
    print('Senha incorreta')

# Exemplo com not
if senha != '123':
    print('Senha incorreta')

# Exemplo 2
if not senha:
    print('Não digitou a senha')

print(not True) # False
print(not False) # True