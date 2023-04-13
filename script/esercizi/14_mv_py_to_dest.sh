#! bin/bash
#trovare i file .py
fileLocali=$(ls)

#trovare quali sono .txt e visualizzarli
for file in $fileLocali ; do
    if [[ $file = *.py ]] ; then
        #spostarli nella cartella Commonplace-Book/python
        mv $file /home/christian/Documenti/Commonplace-Book/python

    fi
done