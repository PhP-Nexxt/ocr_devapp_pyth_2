# ocr_devapp_pyth_2

Le script main.py du dossier "ocr_devapp_pyth_2" permet de "Scrapper" les informations "produits" du site de démonstration Book to Scrape : https://books.toscrape.com/index.html

Pour créer l'environnement virtuel, créez (par exemple) un dossier "ocr_devapp_pyth_2" sur votre disque
Puis dans l'edit de commande ou le terminal(mac ou linux) placez-vous dans ce dossier, puis utilisez la commande : python(python3 sur mac) -m venv env(ou le nom que vous souhaitez donner à votre environnement virtuel)
Activer ensuite cet environnement virtuel : venv\\env(ou le nom de votre environnement virtuel)\\activate.bat ou sur mac : source env(ou le nom de votre environnement virtuel)/bin/activate
  Note : au terme de l'execution du programme, utiliser la commande deactivate pour sortir de l'environnement virtuel
Utilisez le fichier requierement.txt joint pour installer les package python nécessaires à sa bonne execution dans cet environnement virtuel (pip freeze requirement.txt)
Lancer le script en utilisant la commande python main.py (ou python3) sur mac > Vous pouvez suivre l'avancement du scapping dans le terminal
  Note si vous utiliser un ide utilisez l'interpreteur : Python 3.8.8 64-bit ('base':conda)

Les fichiers .csv par categories se trouvent dans le dossier "csv" crée par le script
Les fichiers "image".jpg se trouvent dans le dossier "image" crée par le script et sont nommées selon le code UPC de chaque livre




