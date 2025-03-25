# Exercicio de Fixação
# Peça ao usuário para digitar seu nome
# Peça ao usuário para digitar sua idade
# Se o nome e a idade forem digitidas:
#   Exiba:
#       Seu nome é {nome}
#       Seu nome invertido é {nome_invertido}
#       Seu nome contém (ou não) espaços
#       Seu nome tem {n} letras
#       A primeira letra do seu nome é {letra}
#       A última letra do seu nome é {letra}
# Se nada for digitado em nome ou idade exiba "Desculpe, você deixou campos vazios."

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')
confirmacao_nome_tem_espaço = ' ' in nome
nome_tem_espaço = ''

if confirmacao_nome_tem_espaço == True:
    nome_tem_espaço = 'contém'
else:
    nome_tem_espaço = 'não contém'


if nome != '' and idade != '':
    print('Entrou')
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome {nome_tem_espaço} espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')