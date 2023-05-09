#! bin/bash
#elimina i file con meno di 100 byte

#prendere i file locali
fileLocali=$(ls)


#ricerca globale nella dir. attuale
for file in $fileLocali
do
#fileSize=$(wc -c $file)
sizeNumber=$(wc -c $file | awk '{print $1;}')
    if [[ $sizeNumber -lt 100 ]] ; then
    echo $file ha $sizeNumber byte
#   commentato per non eliminare file utili
#   rm $file ; echo $file " cancellato"
    fi
done