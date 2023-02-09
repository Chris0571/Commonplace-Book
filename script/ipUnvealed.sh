#!/bin/bash
#   IFS == Internal Field Separator,saving the old one is a best practice to not lose the default one
OLD_IFS="$IFS"

# new IFS
IFS=.

echo -n "Inserisci il tuo IP: "
# ex 192.168.1.1
read ip1 ip2 ip3 ip4

IFS="$OLD_IFS"
# restore the default
echo "Il tuo IPv4:"
echo " ip1 -> $ip1"
echo " ip2 -> $ip2"
echo " ip3 -> $ip3"
echo " ip4 -> $ip4"
