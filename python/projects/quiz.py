import time

is_playing = input("Vuoi giocare? ")
PUNTI = 0
if is_playing.lower() != "si":
    print("Ok ma stai calmo")
    quit()
print()


print("Da dove deriva il nome di Python?")
print("A } Dal 'python' della famiglia pythonidae dei rettili")
print("B } Dallo show televisivo Monty Python's Flying Circus")
domanda = input("Risposta: ")

if domanda.lower() == "b":
    print("Corretto")
    time.sleep(1)
    PUNTI += 1
else:
    print("Nein")
    time.sleep(1)
print()


print("Quali tra queste non è una libreria Python")
print("A } math")
print("B } random")
print("C } chatgpt")
print("D } datetime")
domanda = input("Risposta: ")

if domanda.lower() == "c":
    print("Corretto")
    time.sleep(1)
    PUNTI += 1
else:
    print("Sei un'ignorante!")
    time.sleep(1)
print()


print("Quali sono i tipi di dati primitivi in Python?")
print("A } string, int, float, bool")
print("B } list, tuple, set, dict")
print("C } char, double, long, short")
print("D } void, null, Nan, undefined")
domanda = input("Risposta: ")

if domanda.lower() == "a":
    print("Corretto")
    time.sleep(1)
    PUNTI += 1
else:
    print("Cambia lavoro")
    time.sleep(1)
print()


print("Qual è il metodo utilizzato per aggiungere un elemento alla fine di una lista in Python?")
print("A } add()")
print("B } push()")
print("C } append()")
print("D } extend()")
domanda = input("Risposta: ")

if domanda.lower() == "c":
    print("Corretto")
    time.sleep(1)
    PUNTI += 1
else:
    print("Arrenditi")
    time.sleep(1)
print()

print("Quale è il simbolo usato per definire una funzione in Python?")
print("A } ::")
print("B } =>")
print("C } ->")
print("D } =")
domanda = input("Risposta: ")

if domanda.lower() == "c":
    print("Corretto")
    time.sleep(1)
    PUNTI += 1
else:
    print("Vai a studià va..")
    time.sleep(1)
print()

print("Quale operatore viene utilizzato in Python per l'assegnazione di valore ad una variabile?")
print("A } =")
print("B } ==")
print("C } ===")
print("D } equal_to")
domanda = input("Risposta: ")

if domanda.lower() == "a":
    print("Corretto")
    time.sleep(1)
    PUNTI += 1
else:
    print("Se hai sbagliato questa stai messo male")
    time.sleep(1)
print()

print("Qual è il risultato dell'esecuzione del seguente codice Python?\n>>>x = 5\n>>>if x > 2:\n>>>print('x è maggiore di 2')")
print("A } Viene stampato 'x è maggiore di 2'")
print("B } Viene sollevata un'eccezione di tipo 'SyntaxError'")
print("C } Non viene stampato nulla perché l'if non è soddisfatto.")
domanda = input("Risposta: ")

if domanda.lower() == "b":
    print("Corretto")
    time.sleep(1)
    PUNTI += 1
else:
    print("Torna a studià che è meglio")
    time.sleep(1)
print()

print()
print("Hai totalizzato un puntrggio di " + str(PUNTI) + ' su 7')
time.sleep(2.5)
quit()
