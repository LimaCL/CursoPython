"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para paramêtros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""

def Print():
    print('Várias')


def saudacao(nome):
    print(f'Olá {nome}')

    
def saudacao2(nome='Sem nome'):
    print(f'Olá {nome}')

Print()
saudacao('Leandro')
saudacao2()