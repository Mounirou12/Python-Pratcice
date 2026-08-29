def count_positives_sum_negatives(arr):
    return  [
        # PREMIER ÉLÉMENT : Nombre de positifs
        len(  # 4. len() compte le nombre d'éléments dans la liste
            list(  # 3. list() convertit l'itérateur en liste
                filter(  # 2. filter() garde seulement les éléments satisfaisant la condition
                    lambda x: x > 0,  # 1. lambda est une fonction anonyme qui vérifie si x > 0
                    arr  # La liste à filtrer
                )
            )
        ),
        
        # DEUXIÈME ÉLÉMENT : Somme des négatifs
        sum(  # 4. sum() additionne tous les éléments de la liste
            list(  # 3. list() convertit l'itérateur en liste
                filter(  # 2. filter() garde seulement les éléments satisfaisant la condition
                    lambda x: x < 0,  # 1. lambda est une fonction anonyme qui vérifie si x < 0
                    arr  # La liste à filtrer
                )
            )
        )
    ] if len(arr) > 0 else []  # Si la liste est vide, retourner une liste vide


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))