import csv
import os
import time

path = os.getcwd()
start_time = time.time()
PRICE_MAX = 500


def get_data_csv():
    """
    Fonction qui permet d'extraire les données du fichier Actions1.csv
    """
    csv_path = os.path.join(path, "Actions1.csv")
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        list_actions = list(reader)
        return list_actions


def modify_list_csv(data1):
    """
    2)
    Fonction qui garde les valeurs de price superieur à 1.
    """
    new_list = [c for c in data1 if float(c['price']) > 1]
    return new_list


def add_value_csv(data2):
    """
    3)
    Fonction qui calcul et ajoute des valeurs dans le champ total_benefice
    """
    for data_csv in data2:

        value_price = float(data_csv['price'])
        pourcentage = float(data_csv['profit'])
        data_csv['total_benefice'] = value_price * (pourcentage / 100)

    return data2


def sort_list_data(data3):
    """
    4)
    Fonction qui trie la liste
    reverse=False = Petit au plus grand
    """
    list_sort = sorted(data3, key=lambda x: float(x['price']), reverse=True)

    return list_sort


def delete_identical_number(data4):
    """
    5)
    Fonction qui compare les valeurs en double pour le champ price et
    garde la valeur la plus haute
    """
    new_list = []
    for data1 in data4:
        if new_list:
            info_new_list = new_list[-1]
            result_price_new_list = int(float(info_new_list['price']) * 10)
            result_price_modify1 = int(float(data1['price']) * 10)
            if result_price_new_list == result_price_modify1:
                result_profit_new_list = float(info_new_list['profit'])
                result_profit_modify1 = float(data1['profit'])
                if result_profit_modify1 > result_profit_new_list:
                    del new_list[-1]
                    new_list.append(data1)
            else:
                new_list.append(data1)
        else:
            new_list.append(data1)
    return new_list


def generate_best_combinations(data5):
    """
    5)
    Fonction qui permet de créer un tableau à deux dimensions
    les données de data5 sont ensuites calculées et placées dans le tableau selon leurs valeurs
    une fois trerminé, une boucle remonte les listes en partant de la fin et selectionne l'action qui correspond
    puis affiche le résultat.
    """
    pm = PRICE_MAX * 100
    n = len(data5)
    price = [int(float(c['price']) * 100) for c in data5]
    tt_benefice = [float(c['total_benefice']) for c in data5]

    # Créer un tableau à deux dimensions pour stocker les résultats intermédiaires
    t = [[0 for x in range(pm + 1)] for x in range(n + 1)]
    # Parcourir le tableau et calculer les résultats intermédiaires
    for i in range(n + 1):
        for p in range(pm + 1):
            if i == 0 or p == 0:
                t[i][p] = 0
            elif price[i - 1] <= p:
                t[i][p] = max(tt_benefice[i - 1] + t[i - 1][p - price[i - 1]], t[i - 1][p])
            else:
                t[i][p] = t[i - 1][p]

    # Trouver la liste d'actions sélectionnées en remontant le tableau à partir de la dernière cellule
    selected_actions = []
    p = pm
    i = n
    while i > 0 and p > 0:
        if t[i][p] != t[i - 1][p]:
            selected_actions.append(data5[i - 1])
            p -= price[i - 1]
        i -= 1
    # Afficher les résultats
    cost = sum([float(a['price']) for a in selected_actions])
    benefit = sum([float(a['total_benefice']) for a in selected_actions])
    print("Coût d'achat:", cost)
    print("Bénéfice:", benefit)
    print("Liste des actions:")
    for a in selected_actions:
        print(f"{a['name']}: Coût: {a['price']} : Pourcentage: {a['profit']} : bénéfices: {a['total_benefice']}")


list_csv1 = get_data_csv()
list_csv2 = modify_list_csv(list_csv1)
list_csv3 = add_value_csv(list_csv2)
list_csv4 = sort_list_data(list_csv3)
list_csv5 = delete_identical_number(list_csv4)
generate_best_combinations(list_csv5)