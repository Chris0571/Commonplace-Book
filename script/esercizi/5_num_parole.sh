#!bin/bash
#assegnare una variabile per la stringa
echo inserisci una stringa di più parole
read stringa

#contare le parole
echo $stringa > numeroParole
wc -w ./numeroParole
rm ./numeroParole

