#!bin/bash
#prendere in input una lista di nomi e stamparla
echo dammi la lista!
read lista 
nomi=$(cat $lista)

for nome in $nomi
do
    if [[ $nome = "Michele" ]]; then
    echo "Trovato!"
    break
    fi
done



