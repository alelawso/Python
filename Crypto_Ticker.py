#Resources
#https://www.youtube.com/watch?v=w6JqNyHNQnQ
#https://www.youtube.com/watch?v=jOfbQnnllCw
#https://www.tutorialspoint.com/How-to-print-current-date-and-time-using-Python

# importing libraries
from bs4 import BeautifulSoup
import requests
import datetime

def crypto_price(coin):
    # url of the bit coin price
    url = 'https://www.google.com/search?q='+coin+'+price'
    # method to get the price of bitcoin
          
    # getting the request from url 
    HTML = requests.get(url)
      
    # Parse the HTML 
    soup = BeautifulSoup(HTML.text, 'html.parser')
      
    #Finding the current price
    text = soup.find('div', attrs = {'class':"BNeawe iBp4i AP7Wnd"}).find('div', attrs = {'class':"BNeawe iBp4i AP7Wnd"}).text

    #return price
    return coin + ': $' + text

price1 = crypto_price('Bitcoin')
#price2 = crypto_price('Ethereum')
price3 = crypto_price('Cardano')
price4 = crypto_price('Monero')

now = datetime.datetime.now()
print('At '+now.strftime('%H:%M on %A, %B the %dth, %Y'))
print('------------------------------')

print(price1)
print()
#print(price2)
#print()
print(price3)
print()
print(price4)
print()
