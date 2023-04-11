#!bin/bash
#prendere il file e farne una variabile
echo inserisci il nome di un file per verificare se esiste:
read file

#test per vedere se esiste
if [[ -e $file ]] ; then
echo 'il file esiste'
fi