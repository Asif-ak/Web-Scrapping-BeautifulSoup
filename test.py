import requests, bs4

a=requests.get('http://www.tsinghua.edu.cn/publish/hyen/1694/2011/20110113141747864991749/20110113141747864991749_.html')
#print(a.text)
soup=bs4.BeautifulSoup(a.text,'lxml')
title=soup.select('div')
#print(title)
for titles in title:
    print(titles.text)