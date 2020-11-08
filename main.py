
class DataSet:
    """Контейнер для хранения элементов"""
    def __init__(self, data: dict = {}):
        try:
            if not isinstance(data, dict):
                raise ValueError
            else:
                self.__data = data
        except ValueError:
            print('Ошибка присоздании экземпляра! Контейнер пуст')
            self.__data = {}

    def __setitem__(self, key, value):
        try:
            self.__data[key] = value
        except TypeError:
            print(f'{type(key)} не может быть ключом')

    def __getitem__(self, item):
        try:
            return self.__data[item]
        except KeyError:
            print('Данный ключ отсутствует')


data = DataSet()
data['key'] = 'value'
print(data['key2'])
