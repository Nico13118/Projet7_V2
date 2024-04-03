from itertools import combinations
import time
import csv
import os

start_time = time.time()
path = os.getcwd()
MAX = 500


def get_data_csv():
    """ Fonction qui permet d'extraire les données du fichier Action.csv

    : return : list_actions
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
    list_sort = sorted(data3, key=lambda x: float(x['profit']), reverse=True)

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


def generate_combinations(data5):
    total_purchase_action = 0
    total_profit = 0
    best_combinations = []
    length = len(data5)
    list_data1 = list(range(0, length))  # indice de 0 à (20 exclus)
    ll = length
    result_ll = 0
    list_j = []
    aa = True
    while aa:
        j = list(range(0, ll))
        info_price = [float(data5[c]['price']) for c in j]
        info_profit = [float(data5[c]['total_benefice']) for c in j]
        temp_total_purchase_action = sum(info_price)
        temp_total_profit = sum(info_profit)
        if temp_total_purchase_action <= MAX:
            if list_j:
                if temp_total_purchase_action > total_purchase_action:
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
                print("total d'achat", temp_total_purchase_action)
                print("total bénéfice", temp_total_profit)
                print()
        ll -= 1
        if ll == 0:
            aa = False

    list_data3 = combinations(list_data1, result_ll)
    for i in list_data3:
        sum_i = sum(i)
        info_profit = [float(data5[c]['total_benefice']) for c in i]
        temp_total_profit = sum(info_profit)
        if temp_total_profit > total_profit:
            info_price = [float(data5[c]['price']) for c in i]
            temp_total_purchase_action = sum(info_price)
            if temp_total_purchase_action <= MAX:
                select_action = [data5[c] for c in i]
                best_combinations = select_action  # Liste des actions
                total_profit = temp_total_profit  # Total profit
                total_purchase_action = temp_total_purchase_action  # Total d'achat d'action
                print("total d'achat", total_purchase_action)
                print("total bénéfice", total_profit)
                print()
        if sum_i >= MAX + 700:
            break

    return [total_purchase_action, total_profit, best_combinations]


list_csv1 = get_data_csv()
list_csv2 = modify_list_csv(list_csv1)
list_csv3 = add_value_csv(list_csv2)
list_csv4 = sort_list_data(list_csv3)
list_csv5 = delete_identical_number(list_csv4)
final_result = generate_combinations(list_csv5)

print("Coût d'achat:", final_result[0])
print("Bénéfice:", final_result[1])
print("Liste des actions:")
for a in final_result[2]:
    print(f"{a['name']}: Coût: {a['price']} : Pourcentage: {a['profit']} "
          f": bénéfices: {a['total_benefice']}")

end_time = time.time()
result_time = end_time - start_time
print(f"Temps d'exécution : {result_time} seconde(s)")
