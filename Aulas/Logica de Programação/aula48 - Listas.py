"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend +
"""

#      +01234
#      -54321

# string = 'ABCDE' # 5 caracteres (len)

# lista = ['HOJE', 'AMANHÃ']
# print(lista)
# lista.append('ONTEM')
# print(lista)
# print(lista[2])

# #        0   1   2   3   4   5
# lista = [10, 20, 30, 40]
# # lista[2] = 300
# # del lista[2]
# # print(lista)
# # print(lista[2])
# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append(70)
# ultimo_valor = lista.pop(3)
# print(lista, 'Removido,', ultimo_valor)

# #        0   1   2   3
# lista = [10, 20, 30, 40]
# lista.append('Luiz')
# nome = lista.pop()
# lista.append(1233)
# del lista[-1]
# # lista.clear()
# lista.insert(100, 5)
# print(lista[4])

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)

# lista_a = ['Luiz', 'Maria', 1, True, 1.2]
# lista_b = lista_a.copy()

# lista_a[0] = 'Qualquer coisa'
# print(lista_a)
# print(lista_b)