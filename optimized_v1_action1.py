
def start_optimized_v1_functions(list_csv5=None, info_price_max=None):
    result = search_show_result(list_csv5, info_price_max)
    return result


def create_modify_table(pm, n, price, result_profit):
    """
    Fonction qui permet de créer un tableau à deux dimensions, les données sont ensuite
    calculées et placées dans le tableau selon leur valeur.
    Function that creates a two-dimensional array, data is then calculated and placed in
    the array according to their value.
    """
    # Créer un tableau à deux dimensions pour stocker les résultats intermédiaires
    t = [[0 for x in range(pm + 1)] for x in range(n + 1)]
    # Parcourir le tableau et calculer les résultats intermédiaires
    for i in range(n + 1):
        for p in range(pm + 1):
            if price[i - 1] <= p:
                t[i][p] = max(result_profit[i - 1] + t[i - 1][p - price[i - 1]], t[i - 1][p])
            else:
                t[i][p] = t[i - 1][p]
    return t


def search_show_result(info_data, p_max):
    """
    Fonction qui recherches les actions selon les informations dans le tableau puis affiche
    le résultat.
    Function that searches for stocks based on information in the array and displays
    the result.
    """
    price_max = p_max
    pm = int(price_max) * 100
    n = len(info_data)
    price = [int(float(c['price']) * 100) for c in info_data]
    result_profit = [float(c['result_profit']) for c in info_data]

    t = create_modify_table(pm, n, price, result_profit)

    # Trouver la liste d'actions sélectionnées en remontant le tableau à partir de la dernière cellule
    selected_actions = []
    p = pm
    i = n
    while i > 0 and p > 0:
        if t[i][p] != t[i - 1][p]:
            selected_actions.append(info_data[i - 1])
            p -= price[i - 1]
        i -= 1
    sum_price = sum([float(a['price']) for a in selected_actions])
    sum_result_profit = sum([float(a['result_profit']) for a in selected_actions])
    return [selected_actions, sum_price, sum_result_profit]
