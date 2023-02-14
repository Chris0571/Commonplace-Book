#! /bin/bash


if [[ -f $1 ]] ; then
echo 'Il file richiamato è un documento regolare!'
    elif [[ -d $1 ]] ; then
    echo 'Il file richiamato è una cartella!'
        elif [[ -h $1 ]] ; then
        echo 'Il file richiamato è un collegamento!'
            else
            echo 'Errore - il file non esiste'
fi
