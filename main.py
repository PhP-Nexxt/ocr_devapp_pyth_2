# Openclassroom - Dev Appli Python - Projet 2

# Import des packages Python
import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv

#git add nom_du_fichier    = stage
#git commit -m "Description du changement"     = Repository
#git push -u origin main    = depot GitHub

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


    en_tete = [title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url]

    with open('book_to_scrape.csv', 'w') as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=',')
        writer.writerow(en_tete)
        for title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url in zip(title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url):
            ligne = [title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url]
            writer.writerow(ligne)

        #Ligne indice pour ecrire sur csv
    with open('book_to_scrape1.csv' + '/' + title + '/' + price_including_tax + '/' + price_excluding_tax + '/' + number_available + '/' + product_description + '/' + category + '/' + review_rating + '/' + image_url + '.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)




    # Ligne indice pour ecrire sur csv
    '''with open('book_to_scrape.csv' + '/' + universal_product_code + '/' + title + '.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)'''





    # Ligne pour recuperer les variables une a une >
    # price_excluding_tax = soup.find_all("td")[2].get_text()
    # print('Prix hors Taxe :', price_excluding_tax)


   #links = []
    #tds = soup.findAll('a')
    #for td in tds:
         #a = td.find('a')
         #link = a['href']
         #links.append('link')
    #print(links)"""



        #soup.find('a', class_="href")
    #print("Lien : ", link)






# Boucle extraction balises html 'a' category produit
    #categorie = soup.find_all('a')
    #for category in categorie:
        #print("Categories :", category.text)


#Boucle extraction balises html 'tr' information produits
    #prodinfo = soup.find_all('tr')
    #for information in prodinfo:
        #print("Info Produit : ", information.text)'''

#description2 = soup.find('p', class_="instock availability")
    #print("Description2 : ", description2.text)

# Boucle extraction balises html 'p' description produit
    #description = soup.find_all('p')
    #for resume in description:
        #print("Description : ", resume.text)