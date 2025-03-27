# « Notre livre, notre média » 

## Créer un logiciel de gestion de médiathèque 

Ces instructions vous guideront pour faire une copie sur votre machine.
Pour assurer d'avoir les versions de python a jour
ensuite copier les dossiers du GitHub

Installer Python : Téléchargez et installez Python (version 3.13 ou supérieure) depuis python.org.

Créer un environnement virtuel : Ouvrez un terminal ou une invite de commande. Naviguez vers le dossier où vous voulez créer votre projet. Exécutez : python -m venv env Activez l'environnement virtuel : Sur Windows : env\Scripts\activate Sur macOS/Linux : source env/bin/activate

## Mise en place

Installation et configuration :
2.	Cloner le dépôt :
```

git clone https://github.com/greggit49/my-mediath-python.git
cd mediatheque
git remote remove origin
```
3.	Installer les dépendances : pip install django pip install pytest

4.Configurer la base de données : Exécutez les migrations : python manage.py makemigrations mediatheque, python manage.py migrate

5.Charger les données de test : Lancer la commande python manage.py loaddata initial_data.json

6.Lancer le serveur de développement : python manage.py runserver

Accéder à l'application : Ouvrez un navigateur et allez à http://127.0.0.1:8000 