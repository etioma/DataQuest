'''
Compute the average app rating for all the 7,197 apps stored in the data set.

1. Initialize a variable named rating_sum with a value of zero.
2. Loop through the apps_data[1:] list of lists (make sure you don't include the header row).
For each of the 7,197 iterations of the loop (for each row in apps_data[1:]):
    - Extract the rating of the app and store it to a variable named rating (the rating has the index number 8).
        Make sure you convert the rating value from a string to a float using the float() command.
    - Add the value stored in rating to the current value of the rating_sum.
3. Divide the rating sum (stored in rating_sum) by the number of ratings to get an average value.
Store the result in a variable named avg_rating.

'''

import csv
arquivo = open('AppleStore.csv', 'r', encoding="utf8")  # abre arquivo csv, e seta o enconding para UTF8
ler = csv.reader(arquivo, delimiter=',')                # lê o arquivo e usa virgula para separar as colunas
appStoreLista = list(ler)                               # transforma a variavel "ler" em uma lista
#print(appStoreLista[0])
#print(appStoreLista[7])
rating_sum = 0
for row in appStoreLista[1:]:                            # lê a partir da segunda linha, porque a primeira é cabeçalho
    rating = float(row[8])                               # acessa o indice 8 da lista, para buscar o rating (Avaliação)
    rating_sum = rating_sum + rating                     # soma todos os rating na variável rating_sum
avg_rating = rating_sum /len(appStoreLista[1:])          # fora do loop, extrai a média das avaliações.
print(avg_rating)                                        # mostra a média


\