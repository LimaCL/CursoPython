"""
Lista de listas e seus índices
"""

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)]
]

# print(salas[1][0]) # Elaine
# print(salas[0][1]) # Helena
# print(salas[2][2]) # Eduarda
# print(salas[2][3][2]) # 20

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)