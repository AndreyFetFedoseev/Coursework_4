class JobVacancy:
    """
    Класс для работы со списком вакансий
    """

    count_vacancies = 0

    def __init__(self, name, salary, url, snippet, employer):
        self.name = name
        if salary is None:
            self.salary = 0
        else:
            if salary.get('from') is not None:
                self.salary = salary.get('from')
                if salary.get('to') is not None:
                    self.salary = salary.get('to')
            else:
                self.salary = salary.get('to')
        self.url = url
        self.snippet = snippet
        self.employer = employer

        JobVacancy.count_vacancies += 1

    def __repr__(self):
        return (f'{self.__class__.__name__}("{self.name}", "{self.employer}", "{self.salary}", "{self.snippet}", '
                f'"{self.url}")')

    def __len__(self, ):
        return JobVacancy.count_vacancies

    def __str__(self):
        return (f'Название вакансии: {self.name}; Работодатель: {self.employer}; Уровень зарплаты: {self.salary}\n'
                f'Требования: {self.snippet}\nСсылка на вакансию: {self.url}'
                )

    @classmethod
    def get_list_vacancy(cls, list_dict_file_vacancies):
        list_vacancy = []
        for dict_vacancy in list_dict_file_vacancies:
            vacancy = cls(dict_vacancy.get('name'), dict_vacancy.get('salary'), dict_vacancy.get('alternate_url'),
                          dict_vacancy.get('snippet').get('requirement'), dict_vacancy.get('employer').get('name'))
            list_vacancy.append(vacancy)
        return list_vacancy

    @staticmethod
    def sorted_top_vacancy(list_obj_vacancy: list, top_n: int):
        """
        Сортировка вакансий по зарплате и выбор top_n самых высокооплачиваемых
        :param list_obj_vacancy: list obj JobVacancy
        :param top_n: int
        :return: list_sort_top_vacancy
        """
        list_sort_vacancy = sorted(list_obj_vacancy, key=lambda x: x.salary, reverse=True)
        list_sort_top_vacancy = list_sort_vacancy[: top_n]
        return list_sort_top_vacancy

    @staticmethod
    def selection_of_vacancies(list_obj_vacancy, salary_range):
        """
        Отбор вакансий по уровню заработной платы
        :param list_obj_vacancy: list obj JobVacancy
        :param salary_range: str
        :return: list selection obj JobVacancy by salary
        """
        list_selection_vacancies = []
        range_salary = salary_range.split('-')
        for vacancy in list_obj_vacancy:
            if min(map(int, range_salary)) < vacancy.salary < max(map(int, range_salary)):
                list_selection_vacancies.append(vacancy)
        return list_selection_vacancies

    @staticmethod
    def print_top_vacancies(list_vacancies, list_selection_vacancies):
        i = 1
        print(f'Всего найдено вакансий: {JobVacancy.count_vacancies}; '
              f'Кол-во вакансий удовлетворяющих диапазону зарплаты: {len(list_selection_vacancies)}')
        for vacancy in list_vacancies:
            print('__________________________________________________________________________________________________')
            input(f'Перейти к {i} вакансии')
            i += 1
            print(
                f'Название вакансии: {vacancy.name}; Работодатель: {vacancy.employer}; '
                f'Уровень зарплаты: {vacancy.salary}\n'
                f'Требования: {vacancy.snippet}\nСсылка на вакансию: {vacancy.url}')
