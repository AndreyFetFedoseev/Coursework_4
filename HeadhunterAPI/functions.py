import json
import requests

def getAreas():
    req = requests.get('https://api.hh.ru/areas')
    data = req.content.decode()
    req.close()
    jsObj = json.loads(data)
    areas = []
    for k in jsObj:
        for i in range(len(k['areas'])):
            if len(k['areas'][i]['areas']) != 0:  # Если у зоны есть внутренние зоны
                for j in range(len(k['areas'][i]['areas'])):
                    areas.append([k['id'],
                                  k['name'],
                                  k['areas'][i]['areas'][j]['id'],
                                  k['areas'][i]['areas'][j]['name']])
            else:  # Если у зоны нет внутренних зон
                areas.append([k['id'],
                              k['name'],
                              k['areas'][i]['id'],
                              k['areas'][i]['name']])
    return areas

def load_files(json_file):
    with open(json_file, 'r') as file:
        data_vacancy = json.load(file)
    return data_vacancy

# areas = getAreas()
# city = {}
# for area in areas:
#     # print(area)
#     if '113' in area:
#         # if int(area[2]) < 1000:
#         city[area[3]] = int(area[2])
# print(city)
# print(city['Новокузнецк'])
# print(areas)
# save_vacancies('country.json', city)