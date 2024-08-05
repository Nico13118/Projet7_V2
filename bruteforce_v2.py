from itertools import combinations
import time
import csv
import os
import sys

start_time = time.time()
path = os.getcwd()
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
    try:
        control_price_max = int(csv_file[0]['PriceMax'])
    except ValueError:
        print("Erreur constatée dans le champ PriceMax, veuillez saisir ")
        print("une valeur numérique dans le fichier input_data.csv")
        sys.exit()
    file_name = csv_file[0]['CsvFileName']
    csv_path = os.path.join(path, file_name)
    control_file = os.path.exists(csv_path)
    if control_file:
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            list_actions = list(reader)
            return list_actions
    else:
        print(f"Nom du fichier renseigné dans input_data.csv = {file_name}")
        print("Le fichier à analyser n'existe pas dans le répertoire Projet7_V2, veuillez")
        print("contrôler votre saisie dans input_data.csv")
        sys.exit()


def modify_list_csv(data1):
    """
    2)
    Fonction qui garde les valeurs de price supérieures à 0.
    Function that keeps values of price greater than 0.
    """
    new_list = [c for c in data1 if float(c['price']) > 0]
    new_list2 = [c for c in new_list if float(c['profit']) > 0]
    return new_list2


def add_value_csv(data2):
    """
    3)
    Fonction qui calcule et ajoute des valeurs dans le champ total_bénéfice.
    Function that calculates and adds values to the total_profit field.
    """
    for data_csv in data2:

        value_price = float(data_csv['price'])
        pourcentage = float(data_csv['profit'])
        data_csv['total_profit'] = value_price * (pourcentage / 100)

    return data2


def sort_list_data(data3):
    """
    4)
    Fonction qui trie la liste.
    Function that sorts the list.
    """
    list_sort = sorted(data3, key=lambda x: float(x['profit']), reverse=True)

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


def generate_combinations(data5, data_0):
    """
    Fonction qui permet de créer plusieurs listes de combinaisons.
    Boucle qui permet de créer une liste de X combinaisons.
    A chaque tour X est déduit de 1.
    Le total d'achat d'action et de bénéfice sont calculés et garde en mémoire le nombre
    de combinaisons qui sera utilisé à la fin de la boucle.
    La nombre de combinaisons se trouvant dans 'result_ll' permet de créer plusieurs listes
    de combinaisons, permettant ainsi d'avoir un résultat plus précis.
    Function that allows to create multiple combination lists.
    Loop that creates a list of X combinations at each iteration.
    At each iteration, X is reduced by 1.
    The total of stock purchases and profits is calculated and stored in memory, as well
    as the number of combinations that will be used at the end of the loop.
    The number of combinations found in 'result_ll' allows to create multiple combination
    lists, thus ensuring a more accurate result.
    """
    total_purchase_action = 0
    total_profit = 0
    best_combinations = []
    length = len(data5)
    list_data1 = list(range(0, length))  # indice de 0 à (X exclus)
    ll = length
    result_ll = 0
    list_j = []
    price_max = int(data_0[0]['PriceMax'])
    aa = True
    while aa:
        j = list(range(0, ll))
        info_price = [float(data5[c]['price']) for c in j]
        info_profit = [float(data5[c]['total_profit']) for c in j]
        temp_total_purchase_action = sum(info_price)
        temp_total_profit = sum(info_profit)
        if temp_total_purchase_action <= price_max:
            if list_j:
                if temp_total_profit > total_profit:
                    list_j = [j]
                    total_purchase_action = temp_total_purchase_action
                    total_profit = temp_total_profit
                    result_ll = ll

            else:
                list_j.append(j)
                total_purchase_action = temp_total_purchase_action
                total_profit = temp_total_profit
                result_ll = ll

        if ll == 0:
            aa = False
        ll -= 1

    list_data3 = combinations(list_data1, result_ll)
    for i in list_data3:
        sum_i = sum(i)
        info_profit = [float(data5[c]['total_profit']) for c in i]
        temp_total_profit = sum(info_profit)
        if temp_total_profit > total_profit:
            info_price = [float(data5[c]['price']) for c in i]
            temp_total_purchase_action = sum(info_price)
            if temp_total_purchase_action <= price_max:
                select_action = [data5[c] for c in i]
                best_combinations = select_action  # Liste des actions
                total_profit = temp_total_profit  # Total profit
                total_purchase_action = temp_total_purchase_action  # Total d'achat d'action
        if sum_i >= price_max + 700:
            break

    return [total_purchase_action, total_profit, best_combinations]


data0 = get_input_data()
list_csv1 = get_data_csv(data0)
list_csv2 = modify_list_csv(list_csv1)
list_csv3 = add_value_csv(list_csv2)
list_csv4 = sort_list_data(list_csv3)
list_csv5 = delete_identical_number(list_csv4)
final_result = generate_combinations(list_csv5, data0)

print("Coût d'achat:", final_result[0])
print("Bénéfice:", final_result[1])
print("Liste des actions:")
for a in final_result[2]:
    print(f"{a['name']}: Coût: {a['price']} : Pourcentage: {a['profit']} "
          f": bénéfices: {a['total_profit']}")

end_time = time.time()
result_time = end_time - start_time
print(f"Temps d'exécution : {result_time} seconde(s)")
