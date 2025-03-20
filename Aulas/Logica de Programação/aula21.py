# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressõa inteira será avaliada naquele valor.
# São considerados falsy
# Também existe o tipo None que é usado para representar um não valor

# AULA SOBRE and (e)

entrada  = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')