"""
    definizione di fattoriale (n!) in matematica
    """
numero_scelto=input('Inserisci un numero: ')

def fattoriale(numero:int)->int:
    """
    un numero moltiplicato se stesso -1 in maniera ricorsifa calcola il fattoriale
    """
    if numero==0:
        return 1
    return numero * fattoriale(numero -1)

print(fattoriale(numero_scelto))
