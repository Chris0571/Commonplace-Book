import random

lista = []
for i in range(1000000):
    lista.append(random.randint(1, 10000000))

print(sorted(lista))
