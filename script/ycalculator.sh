#! /bin/bash

#echo -n "Inserisci la tua data di nascita nel formato gg/mm/aa :"
#IFS=/

echo -n "Inserisci il tuo anno di nascita e calcolerò la tua età: "
read birty
#IFS="$OLD_IFS"

#echo -n "Che anno è: "
date > dataodierna
actualy=`awk '{print substr($4,1,4)}' ./dataodierna`
#echo siamo nell anno $actualy

(( eta = $actualy - $birty ))
echo "Hai $eta anni!"

rm dataodierna
