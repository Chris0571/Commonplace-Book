#! bin/bash
#aggiunge un determinato prefisso per i file che hanno una determinata estensione 

#dichiarazione variabili
read -p "scegli l'estensione " est
read -p "scegli il prefisso " pre
fileLocali=$(ls)

#ciclo esecuzione
for file in $fileLocali$est
    do
    mv $file $pre$file
    echo $file " e stato rinominato " $pre$file
done