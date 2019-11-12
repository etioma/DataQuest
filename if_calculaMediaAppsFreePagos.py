'''
Modify the existing code in the editor on the right to compute the average rating of non-free apps.

1. Change the name of the empty list from free_apps_ratings to non_free_apps_ratings
(the list we defined before the for loop).
2. Change the condition if price == 0.0 to account for the fact that we now want to isolate only the ratings of non-free apps.
3. Change free_apps_ratings.append(rating) to make sure the ratings are appended to the new list non_free_apps_ratings.
4. Compute the average value by summing up the values in non_free_apps_ratings and dividing by the length of this list.
Assign the result to avg_rating_non_free.
5. Optional exercise: Inspect the value of avg_rating_non_free and compare the average with that of
free apps (the average rating of free apps is approximately 3.38 — we computed it in the first screen).
Can we use the average values to say that free apps are better than non-free apps, or vice versa?
'''

'''
import csv
arquivo = open('AppleStore.csv', 'r', encoding="utf8")  # abre arquivo csv, e seta o enconding para UTF8
ler = csv.reader(arquivo, delimiter=',')                # lê o arquivo e usa virgula para separar as colunas
appStoreLista = list(ler)

# free_apps_ratings = []
non_free_apps_ratings = []
for row in appStoreLista[1:]:
    rating = float(row[8])
    price = float(row[5])
    if price != 0.0:
        non_free_apps_ratings.append(rating)
avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)
print(avg_rating_non_free)
'''

import csv
arquivo = open('AppleStore.csv', 'r', encoding="utf8")  # abre arquivo csv, e seta o enconding para UTF8
ler = csv.reader(arquivo, delimiter=',')                # lê o arquivo e usa virgula para separar as colunas
appStoreLista = list(ler)

free_apps_ratings = []                              # cria lista vazia
# non_free_apps_ratings = []
for row in appStoreLista[1:]:                       # percorre lista appStoreLista
    rating = float(row[8])                          # no loop, atribui o valor da avaliação, indice 8 da lista, na variável rating
    price = float(row[5])                           # no loop, atribui o valor do preço, indice 5 da lista, na variável price
    if price == 0.0:                                # teste lógico para saber se a variável price é zero
        free_apps_ratings.append(rating)            # se sim, inseri o valor guardado em rating, na lista free_apps_rating
        #non_free_apps_ratings.append(rating)
#avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)
avg_rating_free = sum(free_apps_ratings) / len(free_apps_ratings)   # Média: soma todos os valores guardados na lista free_apps_ratings e divide pela quantidade(count/len) da lista free_apps_ratings
print(avg_rating_free)                              # mostra o resultado da variavel avg_rating_free
