#!bin/bash
#prendere in input una lista di numeri
echo inserisci i numeri:
read nmbrs

sum=0
#verificare quali sono divisibili per 2 e aggiungerli alla variabile sum
for i in $nmbrs
do
    if (($i % 2 == 1)); then
    sum=$((i + sum))
    fi

done

echo $sum