from numba import jit


def start_optimized_v2_functions(list_csv5=None, info_price_max=None):
    result = search_show_result(list_csv5, info_price_max)
    return result


@jit
def create_modify_table(pm, n, price, sum_result_profit):
    """
    Fonction qui permet de créer un tableau à deux dimensions, les données sont ensuite
    calculées et placées dans le tableau selon leur valeur.
    Function that creates a two-dimensional array, data is then calculated and placed in
    the array according to their value.
    """
    t = [[0 for x in range(pm + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for p in range(pm + 1):
            if price[i - 1] <= p:
                t[i][p] = max(sum_result_profit[i - 1] + t[i - 1][p - price[i - 1]], t[i - 1][p])
            else:
                t[i][p] = t[i - 1][p]
    return t


def search_show_result(data5, p_max):
    """
    Fonction qui recherches les actions selon les informations dans le tableau puis affiche
    le résultat.
    Function that searches for stocks based on information in the array and displays
    the result.
    """
    price_max = p_max
    pm = int(price_max) * 100
    n = len(data5)
    price = [int(float(c['price']) * 100) for c in data5]
    result_profit = [float(c['result_profit']) for c in data5]

    t = create_modify_table(pm, n, price, result_profit)
    selected_actions = []
    p = pm
    i = n
    while i > 0 and p > 0:
        if t[i][p] != t[i - 1][p]:
            selected_actions.append(data5[i - 1])
            p -= price[i - 1]
        i -= 1
    sum_price = sum([float(a['price']) for a in selected_actions])
    sum_result_profit = sum([float(a['result_profit']) for a in selected_actions])
    return [selected_actions, sum_price, sum_result_profit]
