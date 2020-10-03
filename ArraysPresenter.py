from ArraysModel import ArraysModel
from ArraysView import ArraysView


class ArraysPresenter:

    def __init__(self):
        self.model = ArraysModel()
        self.array1 = []
        self.array2 = []
        self.array3 = []
        self.view = ArraysView(self)
        self.view.start()

    def on_generator_button_pressed(self, button_number: int):
        if button_number == 1:
            self.array1 = self.model.generate_random_array()
            self.view.change_array(self.array1, 1)
        elif button_number == 2:
            self.array2 = self.model.generate_random_array()
            self.view.change_array(self.array2, 2)
        else:
            self.array3 = self.model.join_arrays(self.array1, self.array2)
            self.view.change_array(self.array3, 3)

    def on_reverse_button_pressed(self, k1: int, k2: int):
        try:
            self.array3 = self.model.reverse_array_from_to(self.array3, k1, k2)
            self.view.change_array(self.array3, 3)
        except IndexError:
            self.view.show_error("Index out of range")