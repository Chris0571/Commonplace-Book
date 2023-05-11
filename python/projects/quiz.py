import time
import random

domande = {0: 'Vuoi giocare? s/n\n', 1: "Da dove deriva il nome di Python?", 2: "Quali tra queste non è una libreria Python", 3: "Quali sono i tipi di dati primitivi in Python?",
           4: "Qual è il metodo utilizzato per aggiungere un elemento alla fine di una lista in Python?", 5: "Quale è il simbolo usato per definire una funzione in Python?", 6: "Quale operatore viene utilizzato in Python per l'assegnazione di valore ad una variabile?", 7: "Qual è il risultato dell'esecuzione del seguente codice Python?\n>>>x = 5\n>>>if x > 2:\n>>>print('x è maggiore di 2')"}


insulti = ["Nein", "Non sei capace",
           "Vai a studiare un altro linguaggio", "Cambia lavoro", "Arrenditi", "Ancora che ci provi?", "Questo non me l'aspettavo", "Ce la puoi fare!", "press F to pay respect", "Se continui così il tuo score sarà 0"]

# print(len(insulti))

is_playing = input(domande[0])
PUNTI = 0
if is_playing.lower() != "s":
    print("Ok ma stai calmo")
    quit()
print()


print(domande[1] +
      "\nA } Dal 'python' della famiglia pythonidae dei rettili\nB } Dallo show televisivo Monty Python's Flying Circus")
domanda = input("Risposta: ")

if domanda.lower() == "b":
    print("Corretto")
    time.sleep(1)
    PUNTI += 1
else:
    random_n = int(random.randint(0, 10))
    print(insulti[random_n])
    time.sleep(1)
print()


print(domande[2])
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
    random_n = int(random.randint(0, 10))
    print(insulti[random_n])
    time.sleep(1)
print()


print(domande[3])
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
    random_n = int(random.randint(0, 10))
    print(insulti[random_n])
    time.sleep(1)
print()


print(domande[4])
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
    random_n = int(random.randint(0, 10))
    print(insulti[random_n])
    time.sleep(1)
print()

print(domande[5])
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
    random_n = int(random.randint(0, 10))
    print(insulti[random_n])
    time.sleep(1)
print()

print(domande[6])
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
    random_n = int(random.randint(0, 10))
    print(insulti[random_n])
    time.sleep(1)
print()

print(domande[7])
print("A } Viene stampato 'x è maggiore di 2'")
print("B } Viene sollevata un'eccezione di tipo 'SyntaxError'")
print("C } Non viene stampato nulla perché l'if non è soddisfatto.")
domanda = input("Risposta: ")

if domanda.lower() == "b":
    print("Corretto")
    time.sleep(1)
    PUNTI += 1
else:
    random_n = int(random.randint(0, 10))
    print(insulti[random_n])
    time.sleep(1)
print()

print()
print("Hai totalizzato un puntrggio di " + str(PUNTI) + ' su 7')
time.sleep(2.5)
quit()
