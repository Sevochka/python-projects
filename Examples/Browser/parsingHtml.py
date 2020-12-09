import requests, bs4

selector = '#current_conditions-summary > p.myforecast-current-lrg'

res = requests.get('https://forecast.weather.gov/MapClick.php?lat=43.345270009406505&lon=-78.55568002842166#.X9DIMNgzY2w')
res.raise_for_status()
noStarchSoap = bs4.BeautifulSoup(res.text, 'html.parser')
print(noStarchSoap.select_one(selector).getText())