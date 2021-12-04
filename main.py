# Openclassroom - Dev Appli Python - Projet 2

# Import des packages Python
import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv

#git add nom_du_fichier    = stage
#git commit -m "Description du changement"     = Repository
#git push -u origin main    = depot GitHub



#A faire boucle for de recuperation
#for url in category_urls:
#Et imprimer dans la console
# Sans se preocuper de la category pour l'instant


# Url Cible
url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
# Depot de la requete 'Url" dans un objet 'page'
page = requests.get(url)

#script recuperation informatipn 1 page
if page.ok:

    #Création d'un objet "soup" a partir de la page html
    soup = BeautifulSoup(page.text, 'html.parser')

    # Extraction de la variables prix hors taxe
    universal_product_code = soup.find_all("td")[0].get_text()
    print('Upc :', universal_product_code)

    #Extraction du Titre dans la balise html
    title = soup.find('h1')
    print('Titres :', title.text)

    # Extraction de la variables prix avec taxe
    price_including_tax = soup.find_all("td")[3].get_text()
    print('Prix avec Taxe :', price_including_tax)

    # Extraction de la variables prix hors taxe
    price_excluding_tax = soup.find_all("td")[2].get_text()
    print('Prix hors Taxe :', price_excluding_tax)

    # Extraction de la variables nombre disponible
    number_available = soup.find_all("td")[5].get_text()
    print('Nombre disponible :', number_available)

    # Extraction de la variables description_produit
    product_description = soup.find_all("p")[3].get_text()
    print('Description produit :', product_description)

    # Extraction de la variables category
    category = soup.find_all('a')[3].get_text()
    print('Categorie produit :', category)

    # Extraction du rating (Etoile)
    #                   Cle / Valeur                                    #3eme balise 'p' #2eme class
    review_rating = soup.find("div", {"class": "col-sm-6 product_main"}).find_all("p")[2]["class"][1]
    print('Notation :', review_rating + ' Stars')

    #Extraction de l'Url de Image
    image_url = "http://books.toscrape.com/" + soup.findAll('img')[0]['src'][6:]
    image_reference = (title.text.replace('/', '_') + "_image.jpg")
    print('Url image', image_url)

"""
   Ecriture .csv qui ne foncctionne pas 
    with open(f"./csv", "w", encoding="utf-8") as outf:
        outf.write("url;upc;title;price_including_tax;price_excluding_tax;number_available;description;category;rating;image_url")

        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.content, "lxml")

            #Extraction du Titre dans la balise html
            title = soup.find('h1')

            # Extraction de UPC
            upc = soup.find_all("td")[0].get_text()

            # Extraction de la variables prix avec taxe
            price_including_tax = soup.find_all("td")[3].get_text()

            # Extraction de la variables prix hors taxe
            price_excluding_tax = soup.find_all("td")[2].get_text()

            # Extraction de la variables nombre disponible
            number_available = soup.find_all("td")[5].get_text()

            # Extraction de la variables description_produit
            product_description = soup.find_all("p")[3].get_text()

            # Extraction de la variables category
            category = soup.find_all('a')[3].get_text()

            # Extraction du rating (Etoile)
            #                   Cle / Valeur                                    #3eme balise 'p' #2eme class
            review_rating = soup.find("div", {"class": "col-sm-6 product_main"}).find_all("p")[2]["class"][1]

            #Extraction de l'Url de Image
            image_url = "http://books.toscrape.com/" + soup.findAll('img')[0]['src'][6:]
            image_reference = (title.text.replace('/', '_') + "_image.jpg")

            outf.write(url + upc + title + price_including_tax + price_excluding_tax + number_available + product_description + category + review_rating + image_url)
            """





