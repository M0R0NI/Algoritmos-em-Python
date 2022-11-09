import sys # arquivo de hibernação, o windows usa para armazenar os processo em execução.

mytuple = ("Max", 28, "Boston", "Min", "Boston", 28, 17, 28, "Min", "Boston")
print(mytuple)
print(len(mytuple))
print(mytuple.count("Boston"))  # Função count conta o total de elementos iguais dentro de uma lista ou tupla.
print(mytuple.count(17))
print(sys.getsizeof(mytuple), "bytes")

my_tuple = "Igor Moroni", "São Paulo", "Porsche Cayenne"
name, city, car = my_tuple
print(f"\n{name}")
print(car)
print(sys.getsizeof(my_tuple), "bytes")

