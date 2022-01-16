# ocr_devapp_pyth_2

Le script main.py du dossier "ocr_devapp_pyth_2" permet de "Scrapper" les informations "produits" du site de démonstration Book to Scrape : https://books.toscrape.com/index.html

1- Pre-recquis : 
Pour commencer à travailler sur ce projet, créez et activez un environnement virtuel, puis installez ces paquets :
beautifulsoup4==4.9.3
bs4==0.0.1
certifi==2021.5.30
chardet==4.0.0
idna==2.10
lxml==4.6.3
Pillow==8.3.1
requests==2.25.1
soupsieve==2.2.1
urllib3==1.26.6

2- Environnement Virtuel (installation) : 
Pour créer l'environnement virtuel, créez (par exemple) un dossier "ocr_devapp_pyth_2" sur votre disque
Puis dans l'edit de commande ou le terminal(mac ou linux) placez-vous dans ce dossier, puis utilisez la commande : 
```python(python3 sur mac) -m venv env(ou le nom que vous souhaitez donner à votre environnement virtuel)```

Activer ensuite cet environnement virtuel : ```venv\\env(ou le nom de votre environnement virtuel)\\activate.bat ou sur mac : source env(ou le nom de votre environnement virtuel)/bin/activate```

 Note : au terme de l'execution du programme, utiliser la commande deactivate pour sortir de l'environnement virtuel
  
3- Mode d'execution : 
Lancer le script en utilisant la commande python main.py (ou python3) sur mac > Vous pouvez suivre l'avancement du scapping dans le terminal
Note si vous utiliser un ide utilisez l'interpreteur : Python 3.8.8 64-bit ('base':conda)
Les fichiers .csv par categories se trouvent dans le dossier "csv" crée par le script
Les fichiers "image".jpg se trouvent dans le dossier "image" crée par le script et sont nommées selon le code UPC de chaque livre




