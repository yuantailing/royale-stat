import json
import os
import requests
import settings

def api(url):
    headers = {
        'auth': settings.TOKEN,
    }
    response = requests.request("GET", url, headers=headers)
    assert 200 == response.status_code, url
    data = response.json()
    return data

def clan():
    url = "https://api.royaleapi.com/clan/{:s}".format(settings.CLAN)
    return api(url)

def history(days=7):
    url = "https://api.royaleapi.com/clan/{:s}/history?days={:d}".format(settings.CLAN, days)
    return api(url)

def war_log():
    url = "https://api.royaleapi.com/clan/{}/warlog".format(settings.CLAN)
    return api(url)

if __name__ == '__main__':
    data = {
        'clan': clan(),
        # 'history': history(21),
        'war_log': war_log(),
    }
    with open(os.path.join('www', 'data', 'data.js'), 'w') as f:
        f.write('/**/;var data = ')
        json.dump(data, f)
        f.write(';')
