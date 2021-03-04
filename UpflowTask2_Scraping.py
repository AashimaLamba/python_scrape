import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://media.lesechos.fr/infographie/champions_croissance_2019/')
soup = BeautifulSoup(html, "html.parser")
result = soup.find(id='tableau')
rows = result.findAll("tr")

with open("editors.csv", "wt+", newline="") as f:
    w = csv.writer(f)
    for x in rows:
        final_row = []
        for cell in x.findAll(["td", "th"]):
            final_row.append(cell.get_text())
        w.writerow(final_row)
