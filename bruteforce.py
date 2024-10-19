from itertools import combinations


def start_bruteforce_functions(list_csv5, info_price_max):
    final_result = generate_combination(list_csv5, info_price_max)
    return final_result


def generate_combination(data_csv, p_max):
    p_max = int(p_max)
    n_data = len(data_csv)
    final_list = []
    total_price = 0
    total_result_profit = 0
    for i in list(range(1, n_data)):
        result_comb = combinations(data_csv, i)
        for result in result_comb:
            if len(result) == 1:
                result = result[0]
                action_price, action_result_profit = float(result['price']), float(result['result_profit'])
                if action_price <= p_max:
                    if action_result_profit > total_result_profit:
                        final_list, action_price, total_result_profit = [result], total_price, action_result_profit
            else:
                action_price = [float(c['price']) for c in result]
                if sum(action_price) <= p_max:
                    action_result_profit = [c['result_profit'] for c in result]
                    if sum(action_result_profit) > total_result_profit:
                        final_list = [c for c in result]
                        total_price = sum(action_price)
                        total_result_profit = sum(action_result_profit)
    return [final_list, total_price, total_result_profit]