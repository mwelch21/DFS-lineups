import lxml
import requests
import pandas as pd

nfl_url = r'https://fantasydata.com/NFL_FantasyStats/FantasyStats_Read'

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate'
}

formdata = {
    'sort': 'FantasyPoints-desc',
    'pageSize': '300',
    'filters.position': '2',
    'filters.season': '2020',
    'filters.seasontype': '1',
    'filters.scope': '2',
    'filters.subscope': '1',
    'filters.startweek': '5',
    'filters.endweek': '5',
    'filters.aggregatescope': '1',
    'filters.range': '3',
}

session = requests.session()

response = session.get(url=nfl_url, headers=headers, data=formdata)

data = response.json()

data: pd.DataFrame = pd.json_normalize(data)
