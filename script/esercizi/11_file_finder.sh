#!bin/bash
#visualizzare i file della dir corrente

fileLocali=$(ls)

#trovare quali sono .txt e visualizzarli
for file in $fileLocali
do
if [[ $file = *.txt ]] ; then
    echo $file

fi
done


# oppure semplicemente { ls *.txt }