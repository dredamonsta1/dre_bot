import requests
# import bs4 as bs
from bs4 import BeautifulSoup as bs
import os
# the website to get the image
url = 'http://d.hatena.ne.jp/stmr/touch/20190105'

# download and parse 
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# find all elements wit img tag
image = soup.findAll('img')


if not os.path.exists('kicks'):
    os.makedirs('kicks')


os.chdir('kicks')

x = 0

for image in image:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('kicks-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass