#! bin/bash
#trovare le parole scelte nei file della dir. corrente

#parola da cercare
echo "dammi una parola da cercare"
read wanted

fileLocali=$(ls)


#ricerca globale nella dir. attuale
for file in $fileLocali
do
if [[ -f $file ]] ; then
    cat $file | grep -q $wanted
    echo $wanted " found in " $file

fi
done