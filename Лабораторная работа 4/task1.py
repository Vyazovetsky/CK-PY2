import doctest


class Food:
    def __init__(self, name: str, proteins: int, fats: int, carbohydrates: int):
        """
        Создание базового класса Food
        :param name: название продукта
        :param proteins: кол-во белков в 100 гр
        :param fats: кол-во жиров в 100 гр
        :param carbohydrates: кол-во углеводов в 100 гр
        """
        self.name = name
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __str__(self) -> str:
        return f'Название продукта "{self.name}"'  # унаследованы

    def __repr__(self) -> str:
        return f'Food(name={self.name!r})'  # унаследованы

    def daily_allowance(self):
        """
        :return: возвращает, является ли продукт заменой суточной нормы в физ. потербности
        """
        if self.proteins / 65 >= 1 & self.fats / 70 >= 1 & self.carbohydrates >= 1:
            return "Физиологическая потребность пищи в норме"
        else:
            return "Физиологическая потребность пищи не в норме"


class СaloricСonten(Food):
    def __init__(self, name: str, proteins: int, fats: int, carbohydrates: int):
        """
        Создание дочерниго класса, который считает калорийность продукта на основе базового класса
        """
        super().__init__(name, proteins, fats, carbohydrates)
        self.caloric_conten()

    def caloric_conten(self):
        """
        Метод считает калорийность продукта
        :return:
        """
        return self.proteins * 4 + self.carbohydrates * 4 + self.fats * 9

    def daily_allowance(self):
        """
        Выполнена перегрузка метода базового класса, чтобы учесть еще калорийность продукта
        :return:
        """
        if self.proteins / 65 >= 1 & self.fats / 70 >= 1 & self.carbohydrates >= 1 & self.caloric_conten() / 2500 >= 1:
            return "Физиологическая и энергетическая потребность пищи в норме"
        else:
            return "Физиологическая и энергетическая потребность пищи в норме"


if __name__ == "__main__":
    doctest.testmod()
    pass
