import random


class ArraysModel:

    @staticmethod
    def generate_random_array():
        """Генерируем массив случайного размера от 1 до 10 с случайными элементами от -99 до 99"""
        size = random.randint(1, 10)
        array = [random.randint(-99, 99) for i in range(0, size)]
        return array

    @staticmethod
    def join_arrays(array1: list, array2: list):
        """Создаем новый массив, соединив два других"""
        array = array1.copy()
        array.extend(array2)
        return array

    @staticmethod
    def reverse_array_from_to(array: list, k1: int, k2: int):
        """Проверяем, что k1 и k2 не выходят за границы массива и переворачиваем элементы"""
        if k1 < 0 or k2 >= len(array):
            raise IndexError
        while k2 > k1:
            array[k1], array[k2] = array[k2], array[k1]
            k1 += 1
            k2 -= 1
