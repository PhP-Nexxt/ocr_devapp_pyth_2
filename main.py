# Openclassroom - Dev Appli Python - Projet 2


#Import des paquets necesssaires au script
import requests
from bs4 import BeautifulSoup
from math import ceil
import time
import os
from PIL import Image

#Calcul du temps d'execution du Scrapping
start = time.time()


#Inventaire et Création des categories à scrapper 
website = "https://books.toscrape.com/index.html"
home_response = requests.get(website)
home_soup = BeautifulSoup(home_response.text, "lxml")
list=[]
category_list = home_soup.find("ul", {"class":"nav nav-list"}).find_all("a")
for category in category_list:
    list.append(str(category.text).strip().lower().replace(" ","-"))

#Création du dossier csv si celui-ci n'existe pas
try:
    os.mkdir("csv")
except  OSError as error:
    print(error)

#Creation du dossier image si celui-ci n'existe pas
try:
    os.mkdir("images")
except OSError as error:
    print(error)

#Affichage dynamique de la categorie de Scraping en cours
for category in list[1:]:
    print(f"Starting to scrap {category}.")

    #Definir le nombre de page de la categorie 
    page_count_response = requests.get("https://books.toscrape.com/catalogue/category/books/" + category + "_" + str(list.index(category)+1))
    page_count_soup = BeautifulSoup(page_count_response.text, "lxml")
    product_count = page_count_soup.find("form", {"class" : "form-horizontal"}).find("strong").text
    page_count = ceil(int(product_count)/20)

    #Corriger l'url lorsque le la categorie contient une seule page
    category_urls = []
    i=1
    if page_count > 1:
        category_catalog_url = "https://books.toscrape.com/catalogue/category/books/" + category + "_" + str(list.index(category)+1) + "/page-" + str(i) + ".html"
    else:
        category_catalog_url = "https://books.toscrape.com/catalogue/category/books/" + category + "_" + str(list.index(category)+1) + "/index.html"

    for i in range(1,page_count+1):
        category_response = requests.get(category_catalog_url)

        if category_response.ok:
            category_soup = BeautifulSoup(category_response.text, "lxml")
            for h3 in category_soup.find("ol", {"class" : "row"}).find_all("h3"):
                a = h3.find('a')
                link = a['href']
                category_urls.append("https://books.toscrape.com/catalogue/"+ str(link[9:]))

    #Ecriture des requetes dans le fichier csv  
    with open(f"./csv/{category}.csv", "w", encoding="utf-8") as outf:
        
        #Ecriture des en-tete de colonnes 
        outf.write("url;upc;title;price_including_tax;price_excluding_tax;number_available;description;category;rating;image_url")
        
        #Extraction des éléments demandés
        for url in category_urls:
            response = requests.get(url)
            if response.ok:
                soup = BeautifulSoup(response.content, "lxml")

                title = soup.find("h1").get_text()

                upc = soup.find_all("td")[0].get_text()

                price_excluding_tax = soup.find_all("td")[2].get_text()

                price_including_tax = soup.find_all("td")[3].get_text()

                number_available = soup.find_all("td")[5].get_text()

                description = soup.find("article").find_all("p")[3].get_text().replace(";", "/").strip()

                category = soup.find("ul", {"class" : "breadcrumb"}).find_all("li")[2].text

                rating = soup.find("div", {"class" : "col-sm-6 product_main"}).find_all("p")[2]["class"][1]
                
                #Extraction de l'image liée
                image = soup.find("div", {"class" : "item active"}).img["src"]
                image_url = "http://books.toscrape.com/" + image[6:]
                img = Image.open(requests.get(image_url, stream=True).raw)
                #Ecriture de l'image 
                img.save(f'./images/{upc}.jpg')

                #Ecriture des éléments demandés
                outf.write("\n" + url + ";" + upc + ";" + title + ";" + price_including_tax + ";" + price_excluding_tax + ";" + number_available + ";" + description + ";" + category.replace('\n','') + ";" + rating + ";" + image_url)
                #Affichage dynamique du titre scrappé
                print(f"{title}  : scrapped.")

#Affichage dynamique de fin de script
print("Done.")

#Affichage dynamique du temps d'execution (cf. Ligne 12)
end = time.time()
elapsed = end - start
print(f"temps d'éxécution : {elapsed}")