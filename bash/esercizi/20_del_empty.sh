#! bin/bash

echo "elimino i file vuoti"

find . -type f -empty | while read vuoto
do 
    echo "elimino $vuoto"
    rm $vuoto
done

echo "non ci sono file vuoti"
