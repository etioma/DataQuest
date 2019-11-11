'''
Using the new technique we've learned, compute the average app rating for all of the 7,197 apps stored in our data set.

1. Initialize an empty list named all_ratings.
2. Loop through the apps_data[1:] list of lists (make sure you don't include the header row).
For each of the 7,197 iterations of the loop:
    - Extract the rating of the app and store it to a variable named rating (the rating has the index number 7).
    Make sure you convert the rating value from a string to a float.
    - Append the value stored in rating to the list all_ratings.
3. Compute the sum of all ratings using the sum() command.
4. Divide the sum of all ratings by the number of ratings, and assign the result to a variable named avg_rating.

'''

import csv
arquivo = open('AppleStore.csv', 'r', encoding="utf8")  # abre arquivo csv, e seta o enconding para UTF8
ler = csv.reader(arquivo, delimiter=',')                # lê o arquivo e usa virgula para separar as colunas
appStoreLista = list(ler)                               # transforma a variavel "ler" em uma lista

all_ratings = []                                        # cria uma lista em branco
for raw in appStoreLista[1:]:                           # loop acessando a lista appStoreLista a partir da segunda linha, porque a primeira é cabeçalho
    rating =float(raw[8])                               # acessa o indice 8 da lista, para pegar o "rating" (avaliação dos clientes)
    all_ratings.append(rating)                          # em cada rating que o loop percorre, acrescenta na lista "all_ratings", que foi criada em branco
    #print(all_ratings)                                 # mostra as avaliações que foram acrescentadas na lista
#print(len(all_ratings))                                # aqui um teste para fazer um count da lista
avg_rating = sum(all_ratings) / len(all_ratings)        # soma todas as avaliações e divide pela quantidade de avaliações que existe na lista, para buscar a média
print(avg_rating)                                       # mostra a média

