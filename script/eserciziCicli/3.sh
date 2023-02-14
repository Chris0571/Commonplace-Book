#! /bin/bash
echo "ogni riga corrisponde al numero dell'elemento inserito"
arg=$1
for arg 
do
    if [[ -f $1 ]] ; then
    echo 'Il file è un documento regolare!'
        elif [[ -d $1 ]] ; then
        echo 'Il file è una cartella!'
            elif [[ -h $1 ]] ; then
            echo 'Il file è un collegamento!'
                else
                echo 'error 404'
    fi
shift
done



