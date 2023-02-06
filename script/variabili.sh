#! /bin/bash
# indica il programma con il quale eseguire il seguente script, quindi la shell


# /Variabili

echo $variabile
# stampa un'eventuale variabile esterna se lanciato come 'source' o se è stata 'export [$variabile]'
# altrimenti non stampa niente


variabile=valore_interno
echo $variabile
# assegnata la variabile e richiamata la stampa, se già ce ne era una la sovrascrive
# se lanciato come 'source' la variabile rimane sovrascritta!


