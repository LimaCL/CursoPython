# INPUT

nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}') # O seu nome é Bryan
print(f'O seu nome é {nome=}') # O seu nome é nome='Bryan' 

# Quando utilizado 'nome=' ele traz o nome da variavel e o conteudo dela

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
print(f'A soma dos números é: {int(numero_1) + int(numero_2)}')