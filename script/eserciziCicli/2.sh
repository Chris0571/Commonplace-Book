#! /bin/bash

echo 'Dimmi il nome di un file:'
read file 

if [[ -f $file ]] ; then
echo 'Il file richiamato è un documento regolare!'
    elif [[ -d $file ]] ; then
    echo 'Il file richiamato è una cartella!'
        elif [[ -h $file ]] ; then
        echo 'Il file richiamato è un collegamento!'
            else
            echo 'error 404'
fi
