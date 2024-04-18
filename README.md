## AlgoInvest&Trade - Algorithme de Maximisation des Bénéfices

### Auteur : Nicolas Sylvestre

### Contact : sylvestrenicolas@sfr.fr

## Introduction
### Cet algorithme a pour objectif de calculer et de maximiser les bénéfices financiers, il est disponible sous 3 versions différentes : bruteforce, optimized_v1, optimized_v2.

## Fonctionnement de l'algorithme
### AlgoInvest&Trade a conçu un algorithme permettant de lire le contenu d'un fichier CSV, de calculer et d'afficher la liste d'actions qui rapportent le plus de bénéfices en fonction de l'investissement initial.
### L'algorithme est implémenté dans trois versions différentes pour offrir une flexibilité et une efficacité maximales :
### - **Version Brute Force** : Cette version utilise une approche de force brute pour calculer les résultats. Cet algorithme peut être plus lent, mais garantit une solution optimale.
### - **Version Optimisée (1)** : Cette version utilise une méthode optimisée pour calculer les résultats tout en garantissant une solution optimale.
### - **Version Optimisée (2)** : Cette version est une autre version optimisée qui vise à améliorer encore les performances de calcul.

## Prérequis
### Avant d'utiliser cet algorithme, assurez-vous d'avoir les éléments suivants installés sur votre système :
## Python
### Assurez-vous d'avoir installé la dernière version de Python. Si ce n'est pas déjà fait, vous pouvez suivre les instructions fournies dans le lien suivant pour installer Python :
### [Guide d'installation Python](https://fr.wikihow.com/installer-Python)

## Git
### Git est utilisé pour la gestion de versions et le suivi des changements dans le code source. Si vous n'avez pas encore installé Git, vous pouvez suivre les instructions fournies dans le lien suivant pour l'installation :
### [Guide d'installation Git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)

## Téléchargement des fichiers.
### Sous Windows, ouvrez une invite de commande (Cmd ou PowerShell) et exécutez les commandes suivantes :
```
cd desktop   
   ```
```
git clone https://github.com/Nico13118/Projet7_V2.git
   ``` 
### Sous Mac / Linux, ouvrez le Terminal et exécutez les commandes suivantes :
```
cd ~/Desktop   
   ```
```
git clone https://github.com/Nico13118/Projet7_V2.git
   ``` 

## Création d'un environnement virtuel dans le repertoire Projet7_V2.
### Sous Windows, exécutez les commandes suivantes (Cmd ou PowerShell) :

```
cd desktop/Projet7_V2
   ``` 
```
python -m venv env
   ``` 

### Sous Mac / Linux, exécutez les commandes suivantes (Terminal) :

```
cd ~/Desktop/Projet7_V2  
   ```
```
python3 -m venv env
   ``` 

## Activez l'environnement virtuel

### Sous Windows, exécutez les commandes suivantes (Cmd ou PowerShell) :

### Invite de commande cmd
```
env\Scripts\activate
   ``` 

### Invite de commande PowerShell
```
env/Scripts/activate
   ``` 

### Sous Mac / Linux, exécutez les commandes suivantes (Terminal) :

```
source env/bin/activate
   ``` 

## Mise à jour du gestionnaire de packages et installation des dépendances.

### Sous Windows, exécutez les commandes suivantes (Cmd ou PowerShell) :

```
python.exe -m pip install --upgrade pip
   ``` 

```
pip install -r requirements.txt
   ``` 

### Sous Mac / Linux, exécutez les commandes suivantes (Terminal) :

```
python3 -m pip install --upgrade pip
   ``` 
```
pip install -r requirements.txt
   ``` 

## Structure du fichier CSV.
### Assurez-vous que votre fichier CSV respecte la structure suivante pour que le programme puisse fonctionner correctement :
### - **name** : Le nom de l'action.
### - **price** : Le prix d'achat de l'action.
### - **profit** : Le bénéfice attendu de l'action.

### Voici un exemple de fichier CSV conforme à cette structure :
```
name,price,profit
Name-Action1,10.01,12.25
Name-Action2,26.04,38.06
   ```
## Paramétrage avant analyse.
### Pour commencer l'analyse d'une liste d'actions, vous devez placer un fichier portant l'extension csv dans le répertoire Projet7_V2.
### Ensuite, indiquez à l'algorithme le fichier à analyser et la valeur maximale d'achat d'action en ouvrant le fichier input_data.csv se trouvant dans le répertoire Projet7_V2 avec un éditeur de texte (par exemple : bloc-notes).
### Remplacez "mon_fichier_a_analyser.csv" par le nom de votre fichier et "valeur_max" par une valeur (par exemple : 500) puis enregistrez les modifications.


## Lancemement d'une analyse.

### Sous Windows, exécutez les commandes suivantes (Cmd ou PowerShell) selon l'algorithme que vous souhaitez utiliser :
```
cd desktop/Projet7_V2
   ```
### Algorithme bruteforce:
```
python.exe bruteforce_v2.py
   ```
### Algorithme optimzed_v1:
```
python.exe optimized_v1_action1.py
   ```
### Algorithme optimzed_v2:
```
python.exe optimized_v2_action1.py
   ```

### Sous Mac / Linux, exécutez les commandes suivantes (Terminal) selon l'algorithme que vous souhaitez utiliser :
```
cd ~/Desktop/Projet7_V2
   ```
### Algorithme bruteforce:
```
python3 bruteforce_v2.py
   ```
### Algorithme optimzed_v1:
```
python3 optimized_v1_action1.py
   ```
### Algorithme optimzed_v2:
```
python3 optimized_v2_action1.py
   ```

### Une fois l'analyse terminée, l'algorithme affiche le résultat, qui comprend les éléments suivants :
### - **Le coût total d'achat des actions** : C'est le montant total dépensé pour l'achat des actions sélectionnées.
### - **Les bénéfices générés** : Il s'agit du bénéfice total généré par les actions sélectionnées.
### - **La liste des actions selectionnées** : Cette liste présente les actions choisies par l'algorithme pour maximiser les bénéfices, avec le nom de l'action, le prix d'achat et le bénéfice associé.

