numeri = [2302, 2310, 2315, 2319, 2336, 2341, 2355, 2384, 2390, 2400, 2409, 2430, 2431, 2432, 2449, 2450, 2478, 2489, 2491, 2495, 6, 17, 80, 88, 91, 94, 97, 98, 105, 117, 125, 130, 153, 158, 172, 186, 188, 214,
          1994, 2038, 2038, 2053, 2055, 2058, 2079, 2083, 2095, 2099, 2103, 2103, 2112, 2114, 2130, 2151, 2152, 2176, 2197, 2238, 2271, 2287, 2295, 2299, 2511, 2511, 2517, 2523, 2524440, 3452, 3455, 0, 7777, 3476, 3477, 3478, 3488, 3488, 3495, 3496, 3504, 3506, 3513, 3515, 3517, 3556, 3556, 3563, 3564, 3570, 3572, 3573, 3583, 3587, 3594, 3620, 3623, 3650, 3656, 3657, 3663, 3664, 3680, 3700, 3705, 3706, 3712, 3713, 3717,  3878, 3880, 3897, 3910]

# input per scegliere l'ordine
scelta = input('inserisci "1" per crescente, "2" per decrescente ')


def selection_sort(lista, ordine):
    # prenede 2 parametri

    # non modifica la lista originale
    # .copy() per salvare una copia nel caso si
    listaa = lista.copy()
    length = len(lista)
    # parametri passati per riferimento
    for elemento in range(length):
        minore = elemento

        for successivi in range(elemento+1, length):
            if listaa[successivi] < listaa[minore]:
                minore = successivi

        listaa[elemento], listaa[minore] = listaa[minore], listaa[elemento]

    if ordine == '1':
        return listaa
    if ordine == '2':
        listaa.reverse()
        return listaa


print(selection_sort(numeri, scelta))
