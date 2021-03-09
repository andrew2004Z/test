import requests
from bs4 import BeautifulSoup
from bit import PrivateKey
import time
def get_bitcoin(page):
    html = requests.get(f'https://lbc.cryptoguru.org/dio/{page}').text
    soup = BeautifulSoup(html, 'lxml')
    sp = soup.find_all('span')
    sp_a = []
    for i in sp:
        sp1 = []
        try:
            sp1.append([i.find('span').get_text()[:-1], i.find_all('a')[1].get_text(), i.find_all('a')[2].get_text()])
            sp_a.append(sp1)
        except:
            pass
    for col, i in enumerate(sp_a):
        key1 = PrivateKey(i[0][0])
        print(col)
        if key1.get_balance() != '0':
            print(i)
start_time = time.time()
get_bitcoin(input())
print("--- %s seconds ---" % (time.time() - start_time))