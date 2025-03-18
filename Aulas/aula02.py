#AULA 02 - PRINT
# Comando PRINT é usado para mostrar alguma informação na Tela

# PODE SER USADOS DIVERSOS ARGUMENTOS (TEXTO, NUMEROS)
print('Comando PRINT é usado para mostrar alguma informação na Tela')
print(10)
print(125.30)
print('---------------')
# EXEMPLO COM SEPARADOR COMANDO sep
print(10, 35, sep="-") # RESULTADO = 10-35
print(25, 25, sep="_") # RESULTADO = 25_25
print(25, 25, sep="/") # RESULTADO = 25/25
print('---------------')
# EXEMPLO COM FINALIZADOR COMANDO end
print(99, 45, sep="-", end="\r\n#")  # RESULTADO = 99-45
print(95, 65, sep="_", end="\nxt") # RESULTADO = #95_65
print(45, 65, sep="/", end="\n") # RESULTADO = xt45/65