from functions import load_files


class JobVacancy:
    """
    Класс для работы со словарем вакансий
    """

    count_vacancies = 0

    def __init__(self, name, salary, url, snippet, employer):
        self.name = name
        if salary is None:
            self.salary = 'Зарплата не указана'
        else:
            if salary.get('from') is not None:
                self.salary = f"От {salary.get('from')}"
                if salary.get('to') is not None:
                    self.salary = f"От {salary.get('from')} до {salary.get('to')}"
            else:
                self.salary = f"до {salary.get('to')}"
        self.url = url
        self.snippet = snippet
        self.employer = employer

        JobVacancy.count_vacancies += 1

    def __repr__(self):
        return (f'{self.__class__.__name__}("{self.name}", "{self.employer}", "{self.salary}", "{self.snippet}", '
                f'"{self.url}")')

    @classmethod
    def get_list_vacancy(cls, list_dict_file_vacancies):
        list_vacancy = []
        for dict_vacancy in load_files(list_dict_file_vacancies):
            vacancy = cls(dict_vacancy.get('name'), dict_vacancy.get('salary'), dict_vacancy.get('alternate_url'),
                          dict_vacancy.get('snippet').get('requirement'), dict_vacancy.get('employer').get('name'))
            list_vacancy.append(vacancy)
        return list_vacancy
