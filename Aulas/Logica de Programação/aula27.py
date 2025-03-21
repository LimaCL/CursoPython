# Fatiamento de Strings
# 012345678
# Olá Mundo
#-987654321
# Fatiamento [i:f:p] [::]
# Obs: a função len retorna qtd de caracteres da str
# : demonstra ao python sobre o fatiamento

variavel = 'Olá mundo'
print(variavel[-4]) # u
print(variavel[4:]) # mundo | Se eu omitir o numero final ele pegará o restante
print(variavel[4:8]) # mund | Sempre colocar 1 numero acima do final, pois Python omite o ultimo numero 7 é o final mas foi colocado 8
print(variavel[0:5]) # Olá m
print(variavel[:5]) # Olá m | Se eu omitir o numero inicial ele pegará tudo do inicio até o limite colocado
print(len(variavel[3])) # 1
print(variavel[0:9:4]) # Omo
print(variavel[::-1]) # odnum álO
