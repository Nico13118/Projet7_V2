## AlgoInvest&Trade - Algorithme de Maximisation des Bénéfices

### Auteur : Nicolas Sylvestre

### Contact : sylvestrenicolas@sfr.fr

### Introduction
Ce programme a pour objectif de calculer et maximiser les bénéfices financiers. 
<br> Il propose deux options d'algorithmes : une version utilisant la méthode brute force pour garantir une solution 
<br> optimale et une version optimisée pour des calculs plus rapides.

### Fonctionnement de l'algorithme
Ces algorithmes sont capables de lire le contenu d'un fichier CSV, de calculer et de sélectionner les actions
<br> les plus rentables en fonction de l'investissement initial, puis d'afficher la liste des actions générant le 
<br> meilleur bénéfice.

### Prérequis
Assurez-vous d'avoir installé la dernière version de Python. Si ce n'est pas déjà fait, vous pouvez suivre les 
<br> instructions fournies dans le lien suivant pour installer Python. 
<br>[Guide d'installation Python](https://fr.wikihow.com/installer-Python)

### Téléchargement des fichiers.  
Cliquez sur le lien suivant pour télécharger l'ensemble des fichiers.
<br> [Télécharger les fichiers](https://github.com/Nico13118/Projet7_V2/archive/refs/heads/master.zip)

_______________________________________________________
# ********** Manipulations sous Windows **********
_______________________________________________________
### Décompresser un fichier zip et le placer sur le bureau.
- Ouvrir l'emplacement ou le fichier zip a été téléchargé.
- Faites un clic droit sur le fichier ***"Projet7_V2-master.zip"*** puis sélectionnez l'option ***"Extraire tout..."***.
- À l'ouverture de la fenêtre, cliquez sur le bouton ***"Extraire"***.
- L’élément décompressé apparaît dans le même répertoire que le fichier ***"Projet7_V2-master.zip"***.
- Faites un double clic sur le répertoire nommé ***"Projet7_V2-master"***.
- Sélectionnez le second répertoire nommé ***"Projet7_V2-master"*** puis placé le sur votre bureau.

### Ouvrir une invite de commande (Cmd ou PowerShell) puis se positionner dans le répertoire ***"Projet7_V2-master"*** :

```
cd desktop/Projet7_V2-master   
   ```

### Création d'un environnement virtuel dans le repertoire ***"Projet7_V2-master"***.

```
python -m venv env
   ``` 

### Activez l'environnement virtuel avec Cmd.

```
env\Scripts\activate
   ``` 
### Activez l'environnement virtuel avec PowerShell.
```
env/Scripts/activate
   ``` 

### Mise à jour du gestionnaire de packages et installation des dépendances (Cmd ou PowerShell) :

```
python.exe -m pip install --upgrade pip
   ``` 

```
pip install -r requirements.txt
   ``` 

### Structure du fichier CSV.
Assurez-vous que votre fichier CSV respecte la structure suivante.

Exemple :
```
name,price,profit
Name-Action1,10.01,12.25
Name-Action2,26.04,38.06
   ```

Pour que le programme puisse analyser un fichier csv, vous devez le placer dans le répertoire ***"Projet7_V2-master\Data"*** présent sur votre bureau.

### Exécution du programme (Cmd ou PowerShell).

```
cd desktop/Projet7_V2-master
   ```
```
python.exe menu.py
   ```

Une fois exécuté, le programme vous proposera de choisir un algorithme (bruteforce / optimized).

Vous pourrez ensuite sélectionner le fichier à analyser et définir le prix d'achat maximum.

Une fois terminé, l'algorithme affichera le résultat, qui comprend les éléments suivants : 
- La liste des actions selectionnées.
- Le coût total d'achat des actions
- Le bénéfice généré

_______________________________________________________
# ********** Manipulations sous Mac \ Linux **********
_______________________________________________________
### Décompresser un fichier zip et le placer sur le bureau.
- Ouvrir l'emplacement ou le fichier zip a été téléchargé.
- Cliquez deux fois sur le fichier .zip 
- L’élément décompressé apparaît dans le même répertoire que le fichier ***"Projet7_V2-master.zip"***. 
- Faites un double clic sur le répertoire nommé ***"Projet7_V2-master"***.
- Sélectionnez le second répertoire nommé ***"Projet7_V2-master"*** puis placé le sur votre bureau.

### Ouvrir le Terminal puis se positionner dans le répertoire ***"Projet7_V2-master"*** :

```
cd ~/Desktop/Projet7_V2-master   
   ```

### Création d'un environnement virtuel dans le répertoire ***"Projet7_V2-master"***.

```
python3 -m venv env
   ``` 

### Activez l'environnement virtuel.

```
source env/bin/activate
   ``` 

### Mise à jour du gestionnaire de packages et installation des dépendances.

```
python3 -m pip install --upgrade pip
   ``` 
```
pip install -r requirements.txt
   ``` 

## Structure du fichier CSV.
Assurez-vous que votre fichier CSV respecte la structure suivante.

Exemple :

```
name,price,profit
Name-Action1,10.01,12.25
Name-Action2,26.04,38.06
   ```
Pour que le programme puisse analyser un fichier csv, vous devez le placer dans le répertoire  
***"Projet7_V2-master\Data"*** présent sur votre bureau.

## Exécution du programme.

```
cd ~/Desktop/Projet7_V2
   ```
```
python3 menu.py
   ```

Une fois exécuté, le programme vous proposera de choisir un algorithme (bruteforce / optimized).

Vous pourrez ensuite sélectionner le fichier à analyser et définir le prix d'achat maximum.

Une fois terminé, l'algorithme affichera le résultat, qui comprend les éléments suivants : 
- La liste des actions selectionnées.
- Le coût total d'achat des actions
- Le bénéfice généré

