from timeit import default_timer as timer

my_string = "Hello, world!"
char = my_string[5]
print(f"O elemento corrrespondente ao número dentro da string é '{char}'.")
substring = my_string[0:5]
print(f"Os elementos corrrespondente aos números dentro da string é '{substring}'.")

my_string1 = "Liberdade"
print(my_string1.upper())
print(my_string1.lower())
print(my_string1.count('e'))
print(my_string1.count('d'))
print(my_string1.count('i'))

my_string3 = "São Paulo terra da garoa"
print(my_string3.replace('terra da garoa', 'terra da prosperidade para aqueles que a buscam!'))
my_list = my_string3.split()
print(my_list)

var = 3.141747
var2 = 7
my_stringD = "A variável é %d" % var 
my_stringF = "A variável é %.3f" % var 
my_string2v = "As variaveis são {} e {}.".format(var, var2)
my_string2v2 = f"As variaveis são {var} e {var2}."
print(my_stringD)
print(my_stringF)
print(my_string2v)
print(my_string2v2)

# Essa é uma maneira de cronometrar o tempo que o programa leva de leitura. Porém, ela é lenta comparada a próx maneira.
print(f"\n\n\nCRONOMETRANDO PROCESSAMENTO\n")
start = timer()
caracter = ["a"] * 15500100
my_string7 = 'sete'
for i in caracter:
    my_string7 += i
stop = timer()
print(stop-start)

# Essa é uma maneira mais rápida.
start = timer()
caracter1 = ["a"] * 15500100
my_string10 = 'sete'
my_string10 = ''.join(caracter1)
stop = timer()
print(stop-start)

