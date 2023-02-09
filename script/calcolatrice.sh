#!/bin/bash

echo Inserisci il primo numero
read num1

echo "Inserisci l'operatore (+,-,*,/): "
read operatore

case $operatore in
+)
echo Inserisci il secondo numero
read num2
risultato=$((num1 + num2))
echo La somma tra i 2 numeri è $risultato;;

-)
echo Inserisci il secondo numero
read num2
risultato=$((num1 - num2))
echo La sottrazione tra i 2 numeri è $risultato;;

\*)
echo Inserisci il secondo numero
read num2
risultato=$((num1 * num2))
echo La moltiplicazione tra i 2 numeri è $risultato;;

/)
echo Inserisci il secondo numero
read num2
risultato=$((num1 / num2))
echo La divisione tra i 2 numeri è $risultato;;
*)
echo Operatore sconosciuto ;;
esac