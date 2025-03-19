#FORMATAÇÃO DE STRING

a = 'A'
b = 'B'
c = 1.1

d = 'D'
e = 'E'
f = 2.1

g = 'G'
h = 'H'
i = 3.1

formato = 'a = {} b = {} c = {}'.format(a, b, c) 
print(formato) # a = A b = B c = 1.1

string = 'd = {} e = {} f = {}'
formato_dois = string.format(d, e, f)
print(formato_dois) # a = D b = E c = 2.1


# PARAMETRO NOMEADO
string = 'd = {nome_um} e = {nome_dois} f = {nome_tres}'
formato_tres = string.format(nome_um=g, nome_dois=h, nome_tres=i)
print(formato_tres) # d = G e = H f = 3.1