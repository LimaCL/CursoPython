"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro
"""

numero_digitado = input('Digite um número inteiro: ')

""" if numero_digitado.isdigit():
    entrada_int = int(numero_digitado)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'
    
    if par_impar:
        par_impar_texto = 'par'

    print(f'O numero {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro') """

""" try:
    entrada_int = int(numero_digitado)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'
    
    print(f'O numero {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro') """

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

entrada = input('Digite a hora do dia: ')

try:
    entrada_int = int(entrada)
    if entrada_int < 24:
        if entrada_int >= 0 and entrada_int <=11:
            print('Bom dia')
        elif entrada_int <= 17:
            print('Boa Tarde')
        else:
            print('Boa noite')
    else:
            print('Não conheço essa hora')
        
except:
    print('Valor digitado não aceito, informe um numero')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
"""

nome = input('Digite o seu primeiro nome: ')

qtd_letras_no_nome = len(nome);

try:
    if qtd_letras_no_nome > 0 and qtd_letras_no_nome <= 4:
          print('Seu nome é curto')
    elif qtd_letras_no_nome <= 6:
         print('Seu nome é normal')
    else:
         print('Seu nome é muito grande')
except:
     print('Informação inválida')