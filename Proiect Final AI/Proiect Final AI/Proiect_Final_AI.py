from bs4 import BeautifulSoup
import requests
import csv

genCarte=['arta-si-design','medicina','beletristica','educatie','istorie']

nrCarti=5
counter=0

for gen in genCarte:

    url = "https://www.librariilealexandria.ro/carte/"+genCarte[counter]

    agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

    pagina = requests.get(url, headers=agent)

    soup= BeautifulSoup(pagina.content, 'html.parser')

    file=open(gen,"w",encoding="utf-8")

    titluri=soup.find_all('h4',{"class":"product-name"})

    autori=soup.find_all('h3',{"class":"product-description"})

    preturi=soup.find_all('p',{"class":"price"})


    for i in range (0,nrCarti):
         
        linie1='Titlu: '+titluri[i].get_text()+'\n'

        linie2='Autor:'+autori[i].get_text()

        linie3='Pret: '+preturi[i].get_text()+'\n'

        file.write(linie1)

        file.write(linie2)

        file.write(linie3)
 
    file.close()

    counter=counter+1

print("GATA")

