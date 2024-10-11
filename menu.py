import os

project_root = os.getcwd()


def show_menu():
    loop = True
    while loop:
        print("-------------Menu-------------")
        print("1) Algorithme BruteForce")
        print("2) Algorithme Optimized V1")
        print("3) Algorithme Optimized V2")
        print("4) Quitter")
        print("------------------------------")
        user_response = input("Quel est votre choix ? : ")

        x = user_response.isdigit()
        if x:
            user_response = int(user_response)
            if user_response == 1:
                selected_file = select_csv_file()
                print("Fichier selectionné = ", selected_file)
            elif user_response == 2:
                print("Choix 2 ok")
            elif user_response == 3:
                print("Choix 3 ok")
            elif user_response == 4:
                print("Choix 4 ok")
            else:
                error_message(info_message="Error_Menu")
        else:
            error_message(info_message="Error_Menu")


def select_csv_file():
    select_file = None
    path = f"{project_root}/Data/"
    info_file = os.listdir(path)
    loop = True
    while loop:

        if info_file:
            print("-------Liste des fichiers à analizer-------")
            i = 0
            for inf_file in info_file:
                i += 1
                print(f"{i}) {inf_file}")
            response = input("Quel fichier souhaitez-vous analizer ?")
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


def error_message(info_message=None, info_path=None):
    if info_message == "Error_Menu":
        print("Erreur ! Vous devez faire un choix entre les valeurs disponible dans le menu.")
    elif info_message == "Error_No_File":
        print(f"Erreur ! Aucun fichier csv n'est présent à l'emplacement suivant : {info_path}")


show_menu()
