import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: '+exc)
# print(res.text[0:250])

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    print(chunk)
    playFile.write(chunk)
playFile.close()