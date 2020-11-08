import requests
from bs4 import BeautifulSoup


URL = "https://www.amazon.com/DJI-Mavic-Air-More-Combo/dp/B086XCGMN7/ref=sr_1_2?crid=3JBJAIYYZY0PP&dchild=1&keywords=dji+mavic+air+2+fly+more+combo&sprefix=dji+mavic+air%2Caps%2C289&sr=8-2"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html5lib")

title = soup.find(id="productTitle")
price = soup.find(id="priceblock_ourprice")

print(title)
print(price)
