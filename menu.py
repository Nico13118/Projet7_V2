import os
import common_functions
import sys
project_root = os.getcwd()


def show_menu():
    loop = True
    while loop:
        print("\n-------------Menu-------------")
        print("1) Algorithme BruteForce")
        print("2) Algorithme Optimized V1")
        print("3) Algorithme Optimized V2")
        print("4) Quitter")
        print("------------------------------")
        user_response = input("\nQuel est votre choix ? : ")

        x = user_response.isdigit()
        if x:
            user_response = int(user_response)
            if user_response == 1:
                selected_file = select_csv_file()
                info_price = get_max_price()
                common_functions.start_common_functions(selected_file, info_price, algorithm_name='bruteforce')
            elif user_response == 2:
                selected_file = select_csv_file()
                info_price = get_max_price()
                common_functions.start_common_functions(selected_file, info_price, algorithm_name='optimized_v1')
            elif user_response == 3:
                selected_file = select_csv_file()
                info_price = get_max_price()
                common_functions.start_common_functions(selected_file, info_price, algorithm_name='optimized_v2')
            elif user_response == 4:
                loop = False
            else:
                error_message(info_message="Error_Menu")
        else:
            error_message(info_message="Error_Menu")
    sys.exit()


def select_csv_file():
    select_file = None
    path = f"{project_root}/Data/"
    info_file = os.listdir(path)
    loop = True
    while loop:

        if info_file:
            print("-------Liste des fichiers à analyzer-------")
            i = 0
            for inf_file in info_file:
                i += 1
                print(f"{i}) {inf_file}")
            response = input("\nQuel fichier souhaitez-vous analyzer ?")
            x = response.isdigit()
            if x:
                response = int(response)
                if response != 0:
                    if response <= i:
                        response -= 1
                        select_file = info_file[response]
                        loop = False
                    else:
                        error_message(info_message="Error_Menu")
                else:
                    error_message(info_message="Error_Menu")
            else:
                error_message(info_message="Error_Menu")
        else:
            error_message(info_message="Error_No_File", info_path=path)
    return select_file


def get_max_price():
    response = None
    loop = True
    while loop:
        response = input("\nSaisissez le prix maximum que vous souhaitez inverstir : ")
        x = response.isdigit()
        if not x:
            error_message(info_message="price_value_error")
        else:
            loop = False
    return response


def error_message(info_message=None, info_path=None):
    if info_message == "Error_Menu":
        print("Erreur ! Vous devez faire un choix entre les valeurs disponible dans le menu.")
    elif info_message == "Error_No_File":
        print(f"Erreur ! Aucun fichier csv n'est présent à l'emplacement suivant : {info_path}")
    elif info_message == "price_value_error":
        print("Erreur ! Vous devez saisir une valeur numérique.")


show_menu()
