#!/bin/bash

echo "Ciao $1, benvenuto nel programma $0"

utenti=$#
echo "Siete in $# "

shift

echo "Gli altri sono $@"