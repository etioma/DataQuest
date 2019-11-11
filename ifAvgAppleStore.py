'''
Complete the code in the editor to find the average rating for free apps.

1. Inside the for loop:
2. Assign the price of an app as a float to a variable named price. The price is the fifth element in each row
(don't forget that the index starts at 0).
3. If price == 0.0, append the value stored in rating to the free_apps_ratings list using the list_name.append()
command (note the free_apps_ratings is already defined in the code editor). Be careful with indentation.
4. Outside the for loop body, compute the average rating of free apps. Assign the result to a variable named avg_rating_free.
The ratings are stored in the free_apps_ratings list.

'''


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