import requests
import json
api_key = 'dd6e423f7f036699ea3033727eef6c94'


def getWeather(city_name):
    res = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}')
    try:
        res.raise_for_status()
    except Exception as e:
        print('There was an error - ' + e)

    if res.status_code == 200:
        return res.text
    elif res.status_code == 404:
        raise Exception('Not Found')
    else:
        raise Exception('Something went wrong - ' + str(res.status_code))


response = json.loads(getWeather('Moscow'))
print(response['weather'])
