#! /bin/bash 

if test -e ./file1.txt ; then 
touch file1.txt
echo 'Federico Alessio Lorenzo
Michele Francesco Samir Angelo'> file1.txt
echo 'Fatto ;)'

    else
    echo 'Impossibile scrivere nel file1.txt'
fi