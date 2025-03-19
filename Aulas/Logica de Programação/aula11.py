# Ordem de execução do cálculo
# 1. (n + n) -> Paranteses
# 2. ** -> Exponenciação
# 3. * / // % -> Multiplicação, Divisão, Divisão Inteira, Resto da divisão
# 4. + - -> Adição e Subtração

# ANTES
conta_1 = 1 + 1 ** 5 + 5
print(conta_1) # 7

# DEPOIS
conta_2 = (1 + 1) ** (5 + 5)
print(conta_2) # 1024