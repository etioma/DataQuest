


import csv
arquivo = open('AppleStore.csv', 'r', encoding="utf8")  # abre arquivo csv, e seta o enconding para UTF8
ler = csv.reader(arquivo, delimiter=',')                # lê o arquivo e usa virgula para separar as colunas
appStoreLista = list(ler)

free_apps_ratings = []
for row in appStoreLista[1:]:
    rating = float(row[8])
    # Complete the code from here
    price = float(row[5])
    if price == 0.0:
        free_apps_ratings.append(rating)
avg_rating_free = sum(free_apps_ratings) /len(free_apps_ratings)
print(avg_rating_free)