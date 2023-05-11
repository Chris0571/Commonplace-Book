test=[1, 2, 21, 6, 90, 5, 7]
def finder(lista:list,to_find:int)->int:
    "cerca in una lista la stringa data e restituisce il suo indice"

    for i, elemento in enumerate(lista):
        if elemento is to_find :
            return i
    return None  

print(finder(test, 59))
    