import requests, bs4

a=requests.get('https://en.wikipedia.org/wiki/Jobs_(film)')
#print(a.text)
soup=bs4.BeautifulSoup(a.text,'lxml')
title=soup.select('h2')
#print(title)
for titles in title:
    print(titles.text)