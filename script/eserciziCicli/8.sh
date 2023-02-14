#! /bin/bash

# LOTTERIA
# uno script che controlli che ci siano meno di 7 argomenti, che siano tutti interi tra 1 e 90, genera 6 numeri casuali, stampa a schermo quanti numeri ha indovinato l'utente
integer='^[0-9]+$'

#array con i numeri scelti?
numeriScelti[]
echo ${#numeriScelti[*]}

# non più di 7 numeri inseriti
if [[ ${#numeriScelti[*]} -le 7 ]] ; then
    echo 'Numeri accettati correttamente' ;   
        else
        echo 'Hai inserito troppi numeri' ; 
fi

# numeri inseriti tra 1 e 90




#generazione di 6 numeri casuali tra 1 e 90
#for (( x = 0 ; x <= 6 ; i += 1 )) ; do

#done


# verifica numeri coincidenti
