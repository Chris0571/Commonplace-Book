#!/bin/bash

#variabile somma e contatore
sum=0
count=0

# Ciclo for per leggere i numeri dall'input e aggiornare la somma e il contatore
for num in "$@"; do
    sum=$((sum+num))
    count=$((count+1))
done

# Calcola la media aritmetica
if (( count > 0 )); then
    average=$(echo "scale=2; $sum/$count" | bc)
    echo "La media aritmetica è: $average"
else
    echo "Non c'è abbastanza dati per calcolare la media aritmetica."
fi