import requests
from bs4 import BeautifulSoup

tanggal = 1
session = requests.Session()
while tanggal <= 30 :
    # html = 'https://www.viva.co.id/indeks/berita/all/2020/6/' + str(tanggal)
    html = 'https://indeks.kompas.com/?site=all&date=2021-03-' + str(tanggal)
    req = session.get(html)
    bs = BeautifulSoup(req.text, 'html.parser')

    # Untuk website viva
    # link = bs.find_all('a', attrs={'class': 'title-content'})

    # Untuk website kompas
    link = bs.find_all('a', attrs={'class': 'article__link'})

    for links in link:
        f = open("list.txt", "a")
        f.write(links['href'] + "\n")
    
    tanggal += 1
f.close()