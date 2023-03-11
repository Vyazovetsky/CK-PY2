import doctest


class Cinema:
    def __init__(self, ticket_price: int, total_seats: int, occupied_places: int):
        """
        Создание и подготовка к работе объекта " Кинотеатр"

        :param ticket_price: цена билета в кино
        :param number_of_seats: общее число мест в кинозале
        :param occupied_places: занятое число мест в кинозале

        Примеры:
        >>> cinema = Cinema(250, 500, 50) # инициализация экземпляра класса
        """
        if not isinstance(ticket_price, int):
            raise TypeError("Цена билета в кино должна быть типа int")
        if ticket_price <= 0:
            raise ValueError("Цена билета в кино должна быть положительным числом")
        self.ticket_price = ticket_price

        if not isinstance(total_seats, int):
            raise TypeError("Общее число мест в кинозале должно быть типа int")
        if total_seats <= 0:
            raise ValueError("Общее число мест в кинозале должно быть положительным числом")
        self.total_seats = total_seats

        if not isinstance(occupied_places, int):
            raise TypeError("Занятое число мест в кинозале должно быть int")
        if occupied_places < 0:
            raise ValueError("Занятое число мест в кинозале не может быть отрицательным числом")
        self.occupied_places = occupied_places

    def is_empty_cinema(self) -> bool:
        """
        Функция, которая проверяет, является ли кинозал пустым

        :return: Является ли кинозал пустым

        Примеры:
        >>> cinema = Cinema(250, 500, 50)
        >>> cinema.is_empty_cinema()
        """
        ...

    def add_new_visitor(self, new_visitors: int) -> None:
        """
        Прибавление посетителя в зал
        :param new_visitors: кол-во новых посетителей
        :raise ValueError: Если кол-во посетителей превышает кол-во свободных мест, то вызывем ошибку

        Примеры:
        >>> cinema = Cinema(250, 500, 50)
        >>> cinema.add_new_visitor(200)
        """
        if not isinstance(new_visitors, int):
            raise TypeError("Новых посетителей должно быть int")
        if new_visitors < 0:
            raise ValueError("Новых посетителей не может быть отрицательным числом")
        ...
    def price_increase(self, increase: int) -> None:
        """
        Повышение цены на билет
        :param increase: сумма повышения

        Примеры:
        >>> cinema= Cinema(250, 500, 50)
        >>> cinema.price_increase(100)
        """
        if not isinstance(increase, int):
            raise TypeError("Число повышения должно быть int")
        if increase < 0:
            raise ValueError("Число повышения не может быть отрицательным числом")
        ...
class Population:
    def __init__(self, children: int, adults: int, elderly_people: int):
        """
        Создание и подготовка к работе объекта " Население"

        :param children: кол-во детей
        :param adults: кол-во взрослых
        :param elderly_people: кол-во пожилых людей

        Примеры:
        >>> city = Population(500, 600, 200) # инициализация экземпляра класса
        """
        if not isinstance(children, int):
            raise TypeError("Число детей должно быть int")
        if children < 0:
            raise ValueError("Число детей не может быть отрицательным числом")
        self.children = children

        if not isinstance(adults, int):
            raise TypeError("Число взрослых должно быть int")
        if adults < 0:
            raise ValueError("Число взрослых не может быть отрицательным числом")
        self.adults = adults

        if not isinstance(elderly_people, int):
            raise TypeError("Число пожилых людей должно быть int")
        if elderly_people < 0:
            raise ValueError("Число пожилых людей не может быть отрицательным числом")
        self.elderly_people = elderly_people

    def which_one_is_bigger(self) -> str:
        """
        Функция, которая определяет, какого населения больше
        :return: Строку с указанием, какого населения больше

        Примеры:
        >>> city = Population(500, 600, 200)
        >>> city.which_one_is_bigger()
        """
        ...
    def which_one_is_less(self) -> str:
        """
        Функция, которая определяет, какого населения меньше
        :return: Строку с указанием, какого населения меньше

        Примеры:
        >>> city = Population(500, 600, 200)
        >>> city.which_one_is_less()
        """
        ...
class Tariff:
    def __init__(self, name: str, price: int, ending: int):
        """
        Создание и подготовка к работе объекта " Тариф"

        :param name: название тарифа
        :param price: цена за срок
        :param ending: срок в днях

        Примеры:
        >>> tariff = Tariff("Чёрный", 650, 30) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название тарифа должно быть str")
        if name == "":
            raise ValueError("Название тарифа не может быть пустым")
        self.name = name

        if not isinstance(price, int):
            raise TypeError("Цена за тариф должна быть int")
        if price < 0:
            raise ValueError("Цена за тариф не может быть отрицательным числом")
        self.price = price

        if not isinstance(ending, int):
            raise TypeError("Срок должен быть int")
        if ending <= 0:
            raise ValueError("Срок должен быть положительным числом")
        self.ending = ending

    def reduce_ending(self, reduce: int) -> None:
        """
        Функция для уменьшения срока дейсвтия тарифа

        :param reduce: кол-во уменьшения дней
        :raise: Если уменьшение превышает исходный срок, то вызываем ошибку

        Примеры:
        >>> tariff = Tariff("Чёрный", 650, 30)
        >>> tariff.reduce_ending(15)
        """
        if not isinstance(reduce, int):
            raise TypeError("Уменьшение срока должнj быть int")
        if reduce < 0:
            raise ValueError("УМеньшение срока не может быть отрицательным числом")

    def rename(self, rename: str) -> None:
        """
        Функция, которая позволяет переименовать тариф
        :return: Измененное название тарифа

        Примеры:
        >>> tariff = Tariff("Чёрный", 650, 30)
        >>> tariff.rename("Очень чёрный")
        """
        if not isinstance(rename, str):
            raise TypeError("Новое имя должно быть str")
        if rename == "":
            raise ValueError("Новое имя не может быть пустым, никаким")

        ...


if __name__ == "__main__":
    doctest.testmod()
