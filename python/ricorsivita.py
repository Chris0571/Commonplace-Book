"""calcola la lunghezza di una stringa in maniera ricorsiva"""

#inserito=input('input the input: ')
def lunghezza(stringa:str)->int:
    """
    restituisce il numero in maniera iterativa"""
    tmp = 0
    for _ in stringa:
        tmp += 1
    return tmp

def lunghezza_ricorsiva(stringa:str)->int:
    """
    restituisce il numero in maniera ricorsiva"""
    if stringa != '':
        return 1 + lunghezza_ricorsiva(stringa[1:])
    else :
        return 0
print('"questa stringa è lunga": ' + str(lunghezza_ricorsiva("questa stringa è lunga")))
#print(lunghezza_ricorsiva(input))


def massimo(lista:list)->int:
    """scrivi la funzione di max() senza usare max"""
    tmp=0
    for num in lista:
        if tmp < num:
            tmp = num
        elif tmp > num:
            continue
    return tmp

def massimo_ricorsivo(lista:list)->int:
    """se il primo elemento è minore del maggiore degli altri ripeti"""
    #caso base
    if len(lista) == 1:
        return lista[0]
    #esecuzione ricorsiva
    if lista[0] < massimo_ricorsivo(lista[1:]):
        return massimo_ricorsivo(lista[1:])
    return lista[0]
print('il maggiore di [1,2,21,6,90,4] è: '+ str(massimo_ricorsivo([1,2,21,6,90,4])))
#print(massimo_ricorsivo(input))


def reverse(stringa:str)->str:
    """somma il risultato al carattere e al risultato precedente
    ciao
    c = c + _
    ic = i + c
    aic = a + ic
    oaic = o + aic
    """
    risultato=''
    for char in stringa:
        risultato = char + risultato
    return risultato

def reverse_ricorsivo(stringa:str)->str:
    """inverte il resto (già invertito) con il primo carattere della stringa"""
    #casi base
    if stringa == '' or len(stringa) == 1:
        return stringa
    #esecuzione
    if len(stringa) > 1:
        soluzione = reverse_ricorsivo(stringa[1:]) + stringa[0]
    return soluzione
print('il contrario di "contrario" è: '+ reverse_ricorsivo('contrario'))
#print(reverse_ricorsivo(input))
