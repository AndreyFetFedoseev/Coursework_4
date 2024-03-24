from class_HeadHunterAPI import HH
# from functions import load_files
from class_job_vacancies import JobVacancy
from class_job_files import JobFiles


HeadhunterAPI = HH()
# with open('country.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
keyword = input('Введите поисковый запрос: ')
country = input('Введите в каком городе искать вакансии: ').capitalize()
top_n = int(input('Введите кол-во вакансий для вывода в топ: '))
salary_range = input('Введите диапазон зарплат(Пример: 100000-150000): ')
# HeadhunterAPI.load_vacancies(keyword, data[country])
city = JobFiles.load_files('country.json')
HeadhunterAPI.load_vacancies(keyword, city[country])
# HeadhunterAPI.save_vacancies('data.json', HeadhunterAPI.vacancies)
JobFiles.save_vacancies('data.json', HeadhunterAPI.vacancies)
# for dict_vacanci in HeadhunterAPI.vacancies:
#     name = dict_vacanci.get('name')
#     department = dict_vacanci.get('department')
#     if department is not None:
#         department = department.get('name')
#     else:
#         department = 'Неизвестен'
#     salary = dict_vacanci.get('salary')
#     if salary is not None:
#         salary = f'{salary.get('from')} - {salary.get('to')}'
#     else:
#         salary = 'Неопределен'
#     snippet = dict_vacanci.get('snippet')
#     print(f'Название вакансии: {name}, работодатель\отдел: {department}, уровень зарплаты: {salary},\n '
#           f'требования: {snippet}')

a = JobVacancy.get_list_vacancy('data.json')
print(a)
b = JobVacancy.selection_of_vacancies(a, salary_range)
c = JobVacancy.sorted_top_vacancy(b, top_n)
print(c)
print(str(c[0]))




# print(HeadhunterAPI.vacancies)
# Создание экземпляра класса для работы с API сайтов с вакансиями
# hh_api = HeadHunterAPI()а

# Получение вакансий с hh.ru в формате JSON
# hh_vacancies = hh_api.get_vacancies("Python")

# Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

# Пример работы контструктора класса с одной вакансией
# vacancy = Vacancy("Python Developer", "", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

# Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.delete_vacancy(vacancy)

# Функция для взаимодействия с пользователем
# def user_interaction():
#     platforms = ["HeadHunter"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
#
#     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
#
#     ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
#
#     sorted_vacancies = sort_vacancies(ranged_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)
#
#
# if __name__ == "__main__":
#     user_interaction()

