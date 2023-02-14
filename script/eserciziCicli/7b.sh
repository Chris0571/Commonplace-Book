#! /bin/bash
# controllare se tutti gli argomenti dati siano stringhe o interi

integer='^[0-9]+$'

for arg
do
    if [[ $arg =~ $integer ]] ; then
        echo "L'argomento $arg è un numero" ;

            else
            echo "L'argomento $arg è una stringa" ;
    fi
done