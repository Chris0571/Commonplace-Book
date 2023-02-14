#! /bin/bash
#// controllare se l'argomento datogli sia una stringa o un intero
#echo 'Inserisci un Numero o una Stringa'
#read arg
integer='^[0-9]+$'

    if [[ $1 =~ $integer ]] ; then
        echo "L'argomento è un numero" ;

            else
            echo "L'argomento è una stringa" ;
    fi

