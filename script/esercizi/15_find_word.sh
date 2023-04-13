#! bin/bash
#trovare le parole scelte nei file della dir. corrente

#parola da cercare
echo "dammi una parola da cercare"
read wanted
#read -p 


fileLocali=$(ls)

#ricerca globale nella dir. attuale
for file in $fileLocali
do
if [[ -f $file ]] && grep -q $wanted $file ; then
    cat $file | grep -q $wanted
    echo $wanted " found in " $file
    else 
        echo "not found 7:"
        break
fi
done