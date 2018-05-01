from bs4 import BeautifulSoup
import requests

# https://finance.yahoo.com/quote/AAPL/history?period1=1492984972&period2=1524520972&interval=1d&filter=history&frequency=1d
# load above url
# parse with beautiful soup
# output close dates and price for all dates shown

if __name__ == '__main__':
    # read and parse the html file
    stocks = requests.get(
        'https://finance.yahoo.com/quote/AAPL/history?period1=1492984972&period2=1524520972&interval=1d&filter=history&frequency=1d')
    soup = BeautifulSoup(stocks.text, 'html.parser')

    keys = [header.text for header in soup.find_all(id='YDC-Col1')[0].thead.find_all('th')]
    rows = soup.find_all(id='YDC-Col1')[0].find_all('tr')
    #remove irrelevant information
    rows.pop(0)
    rows.pop()

    for row in rows:
        values = [td.text for td in row.find_all('td')]
        try:
            print('{}, {}'.format(values[0], values[4]))
        except:
            print('Row is invalid: {}'.format(row))