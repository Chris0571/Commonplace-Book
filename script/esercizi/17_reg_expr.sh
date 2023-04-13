#! bin/bash
#Scrivi uno script che controlla tutti i file nella directory corrente e mostra i file che hanno un nome che inizia con una lettera maiuscola

fileLocali=$(ls)

for file in $fileLocali ; do
#filtrare i file con un'espressione regolare 
if [[ $file == [A-Z]* ]]; then
#if [[ $file =~ [A-Z]* ]]; then
echo $file
fi

done