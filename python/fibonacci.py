"""dato un numero di conigli 
    calcola il il numero di conigli 3 anni dopo"""
numero_scelto=int(input('Inserisci un numero: '))

def fibonacci_ricorsiva(anno:int)->int:
    """questa funzione essendo ricorsiva viene eseguita più e più volte
    per soddisfare le richieste della funzione stessa"""
    if anno == 0 or anno == 1:
        return 1
    return fibonacci_ricorsiva(anno -1) + fibonacci_ricorsiva(anno -2)

def fibonacci_iterativa(anno:int)->int:
    """questa funzione risulta molto più veloce nell'esecuzione perchè
    non va a richiamare se stessa al suo interno risultando non ricorsiva"""
    lista=[1,1]
    for indice in range(2,anno +1):
        lista.append(lista[indice -1] + lista[indice -2])
    return lista[-1]

#print(fibonacci_ricorsiva(30))
print(fibonacci_iterativa(numero_scelto))
