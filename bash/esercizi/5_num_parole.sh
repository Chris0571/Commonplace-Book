#!bin/bash
#assegnare una variabile per la stringa
echo Dammi una frase e ti conterò le parole
read stringa

#contare le parole
echo $stringa > numeroParole.txt
cat numeroParole.txt | wc -w 
rm ./numeroParole.txt

