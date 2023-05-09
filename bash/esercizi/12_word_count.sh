#! bin/bash
# prendere un file come variabile
echo "dammi un file e ti conto le parole all'interno"
read file

#contare le parole del file
wc -w $file