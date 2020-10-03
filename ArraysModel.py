import random


class ArraysModel:

    def generate_random_array(self):
        size = random.randint(1, 10)
        array = [random.randint(-99, 99) for i in range(0, size)]
        return array

    def join_arrays(self, array1: list, array2: list):
        array = array1.copy()
        array.extend(array2)
        return array

    def reverse_array_from_to(self, array: list, k1: int, k2: int):
        if k1 < 0 or k2 >= len(array):
            raise IndexError
        reversed_part = array[k1:k2 + 1]
        reversed_part.reverse()
        result = array[:k1] + reversed_part + array[k2 + 1:]
        return result