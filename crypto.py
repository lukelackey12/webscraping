from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = 'https://coinmarketcap.com/all/views/all/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print()

table_rows = soup.findAll("tr")

for row in table_rows[3:8]:
    columns = row.findAll("td")
    name = row.findAll("a")

    name = name[1].text
    symbol = columns[2].text
    current_price = float(columns[4].text.replace('$','').replace(',',''))
    percent_change = float(columns[8].text.strip('%'))
    prev_price = round(current_price / ( 1+ (percent_change/100)),2)

    print(f"Currency Name: {name}")
    print(f"Symbol: {symbol}")
    print(f"Current Price: ${current_price:,.2f}")
    print(f"Percent Change in last 24 hours: {percent_change}%")
    print(f"Corresponding Price: ${prev_price:,.2f}")
    print()
 