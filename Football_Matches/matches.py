from requests import get
from pprint import PrettyPrinter
printer=PrettyPrinter()


headers = { 'X-Auth-Token': 'df653184433b487799db7942366e788d' }

def today_matches():
    url = 'https://api.football-data.org/v4/matches'
    data = get(url, headers=headers).json()['matches']

    for match in data:
        home_team=match['homeTeam']
        away_team=match['awayTeam']
        league=match['competition']
        season=match['season']
        matchday=match['matchday']
        score=match['score']
        status=match['status']
        print('---------------------------------------------------------------------------------------------')
        print(f"{home_team['name']} VS {away_team['name']}  -{status}")
        print(f"\t{score['fullTime']['home']}  -  {score['fullTime']['away']} ")
        print(f"{league['name']}")

def uclstandings():
    url = 'https://api.football-data.org/v4/competitions/2001/standings'
    data = get(url, headers=headers).json()['standings']

    for group in data:
        stage=group['stage']
        name=group['group']
        table=group['table']
        print('---------------------------------------------------------------------------------------------')
        print(f"{stage}")
        print(f"{name}")
        print(f"{table}")


uclstandings()
today_matches()