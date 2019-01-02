# the website to get the image
url = http://d.hatena.ne.jp/stmr/touch

# download and parse 
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# find all elements wit img tag
image = soup.findAll('img')


if not os.path.exists('kicks'):
    os.