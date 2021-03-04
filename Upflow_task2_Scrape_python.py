import requests
import pandas as pd
import xlwt

from bs4 import BeautifulSoup
URL = 'http://media.lesechos.fr/infographie/champions_croissance_2019/'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='tableau')

y = ['rang-cell', 'nom-cell', 'site-cell','annuel moyen-cell','2014-2017-cell', 'Commune-cell', '2017-cell', '2014-cell', '2017-cell', '2014-cell','description-cell']
t = ['A']
e = -1

my_xls=xlwt.Workbook(encoding='utf-8')
my_sheet1 = my_xls.add_sheet("Upflow", cell_overwrite_ok=True)
for x in y:
    a = results.find_all('td', class_= x)
    f = results.find('th', class_= x)
    e = e + 1
    d = 1
    my_sheet1.write(0,e,f.text)
    for b in a:
        my_sheet1.write(d,e,b.text)
        d = d + 1



my_xls.save("results.csv")
             
             
    
      
       
    
        
  

   
