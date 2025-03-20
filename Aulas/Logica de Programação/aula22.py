# Operadores lógicos
# and (e) or (ou) not (não)
# and - Qualquer uma das condições precisam ser verdadeiras
# Se qualquer valor for considerado verdadeir, a expressõa inteira será avaliada naquele valor.
# São considerados falsy
# Também existe o tipo None que é usado para representar um não valor

# AULA SOBRE or (ou)

entrada  = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123'

if entrada == 'E' or entrada == 'e':
    print('Entrar')
else:
    print('Sair')