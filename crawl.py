import json
import os
import requests
import settings
import time


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


if __name__ == '__main__':
    data = clan()
    filename = 'clan-{:d}.json'.format(int(time.time()))
    with open(os.path.join('history', filename), 'w') as f:
        json.dump(data, f)
