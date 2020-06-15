import requests

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

upload_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
headers = {'Authorization': 'AgAAAAAjFoh4AADLW1oDtANzDEaMqnsSqmjbH5U'}


def translate_it_de(text, to_lang):
    with open('DE.txt') as de:
        original_file = de.read()

    params = {
        'key': API_KEY,
        'text': original_file,
        'lang': 'ru'.format(to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    with open('DE_translate.txt', 'w') as f:
        write = f.write(''.join(json_['text']))

        params = {
            'path': 'DE_translate.txt',
            'overwrite': True,
            'fields': ''
        }

    response = requests.get(upload_URL, headers=headers, params=params)

    resp_json = response.json()['href']
    files = {'file': open('DE_translate.txt')}
    requests.put(resp_json, files=files)


def translate_it_es(text, to_lang):
    with open('ES.txt') as es:
        text = es.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': 'ru'.format(to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    with open('ES_translate.txt', 'w') as f:
        write = f.write(''.join(json_['text']))

    params = {
        'path': 'ES_translate.txt',
        'overwrite': True,
        'fields': ''
    }

    response = requests.get(upload_URL, headers=headers, params=params)

    resp_json = response.json()['href']
    files = {'file': open('ES_translate.txt')}
    requests.put(resp_json, files=files)


def translate_it_fr(text, to_lang):
    with open('FR.txt') as fr:
        text = fr.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': 'ru'.format(to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    with open('FR_translate.txt', 'w') as f:
        write = f.write(''.join(json_['text']))

    params = {
        'path': 'FR_translate.txt',
        'overwrite': True,
        'fields': ''
    }

    response = requests.get(upload_URL, headers=headers, params=params)

    resp_json = response.json()['href']
    files = {'file': open('FR_translate.txt')}
    requests.put(resp_json, files=files)


if __name__ == '__main__':
    translate_it_de('text', 'ru')
    translate_it_es('text', 'ru')
    translate_it_fr('text', 'ru')


