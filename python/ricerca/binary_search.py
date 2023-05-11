
numeri=[11, 17, 21, 37, 38, 77, 121, 253, 447]

def binary_search(lista, da_trovare):
    inizio=0
    fine= len(lista)-1
    while fine>=inizio:
        #salvo l'indice della metà della lista
        #caso base + controllo se da_trovare sta prima o dopo
        meta = (inizio+fine) // 2
        if da_trovare == lista[meta]:
            return meta
        elif da_trovare > lista[meta]:
            inizio = meta +1
        elif da_trovare < lista[meta]:
            fine = meta -1
    return None

print(binary_search(numeri, 151))
