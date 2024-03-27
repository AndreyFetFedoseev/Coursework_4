from class_headhunter_api import HH
from class_job_vacancies import JobVacancy
from class_job_files import JobFiles


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    # Создание экземпляра класса для работы с API сайта HeadHunter
    head_hunter_api = HH()

    # Запрашиваем у пользователя параметры для поиска и обработки списка вакансий
    keyword = input('Введите поисковый запрос: ')
    country = input('Введите в каком городе искать вакансии: ').capitalize()
    top_n = int(input('Введите кол-во вакансий для вывода в топ: '))
    salary_range = input('Введите диапазон зарплат(Пример: 100000-150000): ')

    # Загрузка словаря городов из файла в формате JSON
    city = JobFiles.load_files('../data/country.json')

    # Получение вакансий с hh.ru в формате JSON
    head_hunter_api.load_vacancies(keyword, city[country])

    # Сохранение списка вакансий с определенного города в json файл
    JobFiles.save_vacancies('../data/data_vacancies.json', head_hunter_api.vacancies)

    # Обработка списка вакансий
    list_vacancies = JobVacancy.get_list_vacancy('../data/data_vacancies.json')
    selection_vacancies_by_salary = JobVacancy.selection_of_vacancies(list_vacancies, salary_range)
    sort_top_vacancies = JobVacancy.sorted_top_vacancy(selection_vacancies_by_salary, top_n)
    JobVacancy.print_top_vacancies(sort_top_vacancies, selection_vacancies_by_salary)


if __name__ == "__main__":
    user_interaction()
