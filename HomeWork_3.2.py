import requests

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

upload_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
headers = {'Authorization': 'AgAAAAAjFoh4AADLW1oDtANzDEaMqnsSqmjbH5U'}


def translate_it_de(from_file, to_file, to_lang):
    with open(from_file) as de:
        original_file = de.read()

    params = {
        'key': API_KEY,
        'text': original_file,
        'lang': to_lang.format(to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    with open(to_file, 'w') as f:
        write = f.write(''.join(json_['text']))

        params = {
            'path': to_file,
            'overwrite': True,
            'fields': ''
        }

    response = requests.get(upload_URL, headers=headers, params=params)

    resp_json = response.json()['href']
    files = {'file': open(to_file)}
    requests.put(resp_json, files=files)


if __name__ == '__main__':
    translate_it_de('DE.txt', 'DE_translate.txt', 'ru')
    translate_it_de('ES.txt', 'ES_translate.txt', 'ru')
    translate_it_de('FR.txt', 'FR_translate.txt', 'ru')


