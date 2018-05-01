from bs4 import BeautifulSoup
import requests


# https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns
# load the above url
# parse with beautiful soup

    # output top 20 players, include position, team name and total number of touchdowns
if __name__ == '__main__':
    # read and parse the html file
    stats = requests.get(
        'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns')
    soup = BeautifulSoup(stats.text, 'html.parser')

    # Narrowed down to html table
    sortable_content = soup.find_all(id='sortableContent').pop()
    tr = sortable_content.find_all('tr')
    # located headers within the table
    headers = tr[2].find_all('th')
    players = tr[3:23]
    keys = [header.text for header in headers]
    player_data = [[data.text for data in player] for player in players]


    # construct a player dictionary
    player_stats = {}
    for player in player_data:
        player_stats[player[0]] = dict(zip(keys, player))

    # loop on player_stats and print results
    for key, value in player_stats.items():
        print('{}, Position: {}, Team: {}, Touchdowns: {}'.format(key, value['Pos'], value['Team'], value['TD']))
