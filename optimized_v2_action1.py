import csv
import os
import time
from numba import jit

path = os.getcwd()
start_time = time.time()
INPUT_DATA_CSV = "input_data.csv"


def get_input_data():
    csv_path = os.path.join(path, INPUT_DATA_CSV)
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        info_data = list(reader)
        return info_data


def get_data_csv(csv_file):
    """
    Fonction qui permet d'extraire les données du fichier Actions.csv.
    Function that extracts data from the Actions.csv file.
    """
    file_name = csv_file[0]['CsvFileName']
    csv_path = os.path.join(path, file_name)
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        list_actions = list(reader)
        return list_actions


def modify_list_csv(data1):
    """
    2)
    Fonction qui garde les valeurs de price supérieures à 1.
    Function that keeps values of price greater than 1.
    """
    new_list = [c for c in data1 if float(c['price']) > 1]
    return new_list


def add_value_csv(data2):
    """
    3)
    Fonction qui calcule et ajoute des valeurs dans le champ total_bénéfice.
    Function that calculates and adds values to the total_profit field.
    """
    for data_csv in data2:

        value_price = float(data_csv['price'])
        pourcentage = float(data_csv['profit'])
        data_csv['total_benefice'] = value_price * (pourcentage / 100)

    return data2


def sort_list_data(data3):
    """
    4)
    Fonction qui trie la liste.
    Function that sorts the list.
    """
    list_sort = sorted(data3, key=lambda x: float(x['price']), reverse=True)

    return list_sort


def delete_identical_number(data4):
    """
    5)
    Fonction qui compare les valeurs en double pour le champ price et garde la valeur la
    plus haute de profit.
    Function that compares duplicate values for the price field and keeps the highest
    profit value.
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


@jit
def create_modify_table(pm, n, price, tt_benefice):
    """
    Fonction qui permet de créer un tableau à deux dimensions, les données sont ensuite
    calculées et placées dans le tableau selon leur valeur.
    Function that creates a two-dimensional array, data is then calculated and placed in
    the array according to their value.
    """
    t = [[0 for x in range(pm + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for p in range(pm + 1):
            # if i == 0 or p == 0:
            #     t[i][p] = 0
            if price[i - 1] <= p:
                t[i][p] = max(tt_benefice[i - 1] + t[i - 1][p - price[i - 1]], t[i - 1][p])
            else:
                t[i][p] = t[i - 1][p]
    return t


def search_show_result(data5, data_0):
    """
    Fonction qui recherches les actions selon les informations dans le tableau puis affiche
    le résultat.
    Function that searches for stocks based on information in the array and displays
    the result.
    """
    price_max = data_0[0]['PriceMax']
    pm = int(price_max) * 100
    n = len(data5)
    price = [int(float(c['price']) * 100) for c in data5]
    tt_benefice = [float(c['total_benefice']) for c in data5]

    t = create_modify_table(pm, n, price, tt_benefice)
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


data0 = get_input_data()
list_csv1 = get_data_csv(data0)
list_csv2 = modify_list_csv(list_csv1)
list_csv3 = add_value_csv(list_csv2)
list_csv4 = sort_list_data(list_csv3)
list_csv5 = delete_identical_number(list_csv4)
search_show_result(list_csv5, data0)


end_time = time.time()
result = end_time - start_time
print(f"Temps d'exécution : {result} seconde(s)")
