'''
Criando duas lista vazias, para app´s pagos e não pagos, na Apple Store.
Setando os indices de avaliação e preço.
Teste lógico, se preço for zero, inclui a avaliação na lista " free_apps_ratings ", senão inclui na lista "non_free_apps_ratings"
Soma e calcula a média dos das duas lista.
'''
import csv
arquivo = open('AppleStore.csv', 'r', encoding="utf8")  # abre arquivo csv, e seta o enconding para UTF8
ler = csv.reader(arquivo, delimiter=',')  # lê o arquivo e usa virgula para separar as colunas
appStoreLista = list(ler)

free_apps_ratings = []                          # cria lista vazia para apps não pagos
non_free_apps_ratings = []                      # cria lista vazia para apps pagos
for row in appStoreLista[1:]:                   # percorre a lista appSotreLista, desconsidera cabeçalho
    rating = float(row[8])                      # atribui na variavel rating, indice 8 da lista, o valor da avaliação
    price = float(row[5])                       # atribui na variavel price, indice 5 da lista, o valor do app
    if price == 0.0:                            # testa se valor for igual a zero,
        free_apps_ratings.append(rating)        # inseri o valor da avaliação na variavel "free_apps_ratings"
    else:                                       # senão, o app é pago
        non_free_apps_ratings.append(rating)    # inseri o valor da avaliação na variavel "non_free_apps_ratings"
avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)   # Média: soma todas as avaliações e divide pela quantidade(count) de avaliações inseridas na variavel non_free_apps_ratings
avg_rating_free = sum(free_apps_ratings) / len(free_apps_ratings)               # Média: soma todas as avalições e divide pela quantudade (count) de avaliações inseridas na variavel free_apps_ratings
print('Média das avaliações dos Apps pagos na AppleSotre:' , avg_rating_non_free) # mostra os valores da média de apps pagos
print('Média das avaliações dos Apps não pagos na AppleSotre:' , avg_rating_free) # mostra os valores da média de apps não pagos
