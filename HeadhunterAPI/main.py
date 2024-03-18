from class_HeadHunterAPI import HH

HeadhunterAPI = HH()
HeadhunterAPI.load_vacancies('python', 'Самара')
print(HeadhunterAPI.vacancies)
