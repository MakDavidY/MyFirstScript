#importing libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#Specify the url
quote_page = 'https://www.bloomberg.com/quote/SPX:IND'

#query the website and return the html to variable page
page = urlopen(quote_page)

#parse the html using beautifulsoup and store in variable soup
soup = BeautifulSoup(page, 'html.parser')

#take out the <div> of the name and get its value
name_box = soup.find('h1', attrs={'class':'OverviewRow'})
name = name_box.text()
print(name)

#get the index price
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print(price)

#open a csv file with append, so old data won't be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name,price, datetime.now()])
