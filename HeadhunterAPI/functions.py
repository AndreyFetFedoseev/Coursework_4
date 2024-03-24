import json
import requests


def get_areas():
    req = requests.get('https://api.hh.ru/areas')
    data = req.content.decode()
    req.close()
    js_obj = json.loads(data)
    list_areas = []
    for k in js_obj:
        for i in range(len(k['areas'])):
            if len(k['areas'][i]['areas']) != 0:  # Если у зоны есть внутренние зоны
                for j in range(len(k['areas'][i]['areas'])):
                    list_areas.append([k['id'],
                                       k['name'],
                                       k['areas'][i]['areas'][j]['id'],
                                       k['areas'][i]['areas'][j]['name']])
            else:  # Если у зоны нет внутренних зон
                list_areas.append([k['id'],
                                   k['name'],
                                   k['areas'][i]['id'],
                                   k['areas'][i]['name']])
    return list_areas


def load_files(json_file):
    with open(json_file, 'r') as file:
        data_vacancy = json.load(file)
    return data_vacancy


def save_vacancies(files, data):
    with open(files, 'w', encoding='utf-8') as file:
        json.dump(data, file)


areas = get_areas()
city = {}
for area in areas:
    if '113' in area:
        city[area[3]] = int(area[2])
print(city)
print(city['Новокузнецк'])
print(areas)
save_vacancies('country.json', city)
