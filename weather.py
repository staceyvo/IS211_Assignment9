from bs4 import BeautifulSoup
import requests



# https://www.wunderground.com/history/airport/KNYC/2015/4/1/MonthlyHistory.html

# parse with beautiful soup
# output
    # actual temperatures for days in month that passed
    # forecasted temperatures for days that have not


if __name__ == '__main__':
    # read and parse the html file
    weather = requests.get(
        'https://www.wunderground.com/history/airport/KNYC/2015/4/1/MonthlyHistory.html')
    soup = BeautifulSoup(weather.text, 'html.parser')
    observation = 'observations_details'
    # find table with table id
    response = soup.find(id=observation)
    # find all table rows
    response = response.find_all('tr')
    # pop out irrelevant rows
    [response.pop(0) for _ in range(2)]
    # looping on table data to get avg temp for each day
    temps = [[item.text.replace('\n', '') for item in resp.find_all('td')][2] for resp in response]
    day = 0
    for temp in temps:
        day += 1
        print('Day: {}, Temperature: {}'.format(day, temp))
