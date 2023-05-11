frase = "Eaque laborum et nulla aspernatur distinctio. Quasi nihil adipisci ea at aperiam quis accusantium harum. Maxime et dolorem ut velit. Adipisci cupiditate saepe et ipsam veritatis rerum id. Animi ipsa quia autem alias odio quis. Exercitationem a necessitatibus ad architecto provident qui et. Eius illo minima eos. Incidunt nemo numquam quo. Enim placeat placeat omnis perspiciatis. Unde sint et itaque suscipit provident aut vel. Vitae et hic ratione omnis architecto eos distinctio dolorem. Qui ea omnis placeat quis est vel exercitationem. Excepturi perspiciatis perspiciatis magni laboriosam omnis dolore ut voluptatibus. Eaque cumque quas dolore. Magnam praesentium quasi inventore corporis. Corporis quia in voluptas quia voluptas. Et temporibus voluptatem facere cumque. Aut voluptas id laborum consequatur consequatur et facere. Est doloremque quod esse optio. Quia quia consequuntur soluta. Saepe officia impedit eos debitis. Dolor voluptas ipsa vel corporis placeat et quis. Voluptates vel quia veritatis et vel qui. Accusantium tempora expedita repudiandae est. Quia eum nihil repellat. Molestiae perspiciatis earum explicabo vel et velit. Minima culpa consectetur vel laboriosam. Modi fugiat excepturi quia eaque ea inventore esse. Ea quia qui necessitatibus ipsam. Dolore voluptas optio quas maxime necessitatibus eaque. Ea culpa ad dicta sapiente. Delectus dolore incidunt optio libero labore. Rem in dolorem cumque possimus ea. Dolor sed necessitatibus hic voluptas qui. Laborum a id labore et iste magni. Reiciendis nulla explicabo est omnis eveniet. Aperiam eligendi omnis eius enim aut. Qui officia ipsam soluta voluptatem et voluptates. Quidem facilis quia minus molestias neque vitae. Aut qui architecto odio. Totam et non ea maiores deserunt sed facere consequatur. Qui animi doloribus rerum sequi sint ducimus. Illum odit autem ducimus quisquam nam quas nihil enim.Sunt laborum quis maxime consequatur tempora quasi sit et. Voluptas et tempore nostrum autem. Reiciendis molestiae sed aut vero iusto.Et dolores non aliquam facere aspernatur repellat beatae quasi. Ipsam atque earum aut. Eum amet provident perspiciatis molestiae. Nisi similique sunt consequuntur similique assumenda beatae sunt quasi."
lista_parole = frase.split()
usate = []
conteggio_parole = {}


for parola in lista_parole:
    #calcolo di num parole usate
    if parola not in usate:
        usate.append(parola)

    #assegnazione parole al dizionario
    if parola not in conteggio_parole:
        conteggio_parole.update({parola:1})

    if parola in conteggio_parole:
        conteggio_parole[parola] += 1

piu_usata = max(conteggio_parole.items(), key=lambda x: x[1])

print('Numero di parole diverse usate: ')
print(len(usate))
print()
print('Parola più usata :')
print(piu_usata)
#print(piu_usata(conteggio_parole))
