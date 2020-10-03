from tkinter import *
from tkinter import messagebox


class ArraysView:

    def __init__(self, presenter):
        self.presenter = presenter

        # Root
        self.root = Tk()
        self.root.title("Hello, world!")
        self.root.geometry("800x400+500+150")
        self.root.resizable(True, True)

        # Arrays frame
        self.arrays_frame = Frame(self.root, bg="#1f252a", bd=5)
        self.arrays_frame.pack(fill=X, ipady=5)

        # Array 1
        self.array1_title = Label(self.arrays_frame, bg=self.arrays_frame["bg"], fg="White", text="Array 1",
                                  font="Arial 15",
                                  anchor=CENTER)
        self.array1_title.pack(fill=X)

        self.array1_field = Label(self.arrays_frame, bg="white", font="Arial 15")
        self.array1_field.pack(fill=X, padx=5)

        # Array 2
        self.array2_title = Label(self.arrays_frame, bg=self.arrays_frame["bg"], fg="White", text="Array 2",
                                  font="Arial 15",
                                  anchor=CENTER)
        self.array2_title.pack(fill=X)

        self.array2_field = Label(self.arrays_frame, bg="white", font="Arial 15")
        self.array2_field.pack(fill=X, padx=5)

        # Array 3
        self.array3_title = Label(self.arrays_frame, bg=self.arrays_frame["bg"], fg="White", text="Array 3",
                                  font="Arial 15",
                                  anchor=CENTER)
        self.array3_title.pack(fill=X)

        self.array3_field = Label(self.arrays_frame, bg="white", font="Arial 15")
        self.array3_field.pack(fill=X, padx=5)

        # Generator Buttons frame
        self.generator_buttons_frame = Frame(self.root, bg="#102020", bd=5)
        self.generator_buttons_frame.pack(fill=BOTH)

        # Generator button 1
        self.generator_button_1 = Button(self.generator_buttons_frame, bg="gray", fg="White", text="Generate array 1",
                                         font="Arial 15",
                                         command=lambda x=1: self.on_generator_button_pressed(x))
        self.generator_button_1.pack(fill=BOTH, expand=True, side=LEFT, padx=5)

        # Generator button 2
        self.generator_button_2 = Button(self.generator_buttons_frame, bg="gray", fg="White", text="Generate array 2",
                                         font="Arial 15",
                                         command=lambda x=2: self.on_generator_button_pressed(x))
        self.generator_button_2.pack(fill=BOTH, expand=True, side=LEFT, padx=5)

        # Generator button 3
        self.generator_button_3 = Button(self.generator_buttons_frame, bg="gray", fg="White", text="Generate array 3",
                                         font="Arial 15",
                                         command=lambda x=3: self.on_generator_button_pressed(x))
        self.generator_button_3.pack(fill=BOTH, expand=True, side=LEFT, padx=5)

        # Task frame
        self.task_frame = Frame(self.root, bg="#001010", bd=5)
        self.task_frame.pack(fill=BOTH, expand=True)

        # K title frame
        self.k_title_frame = Frame(self.task_frame, bg="#001010")
        self.k_title_frame.pack(fill=X, pady=5)

        # K1 title
        self.k1_title = Label(self.k_title_frame, bg=self.k_title_frame["bg"], fg="White", text="K1", font="Arial 15",
                              anchor=CENTER)
        self.k1_title.pack(fill=BOTH, expand=True, side=LEFT, padx=5)

        # K2 title
        self.k2_title = Label(self.k_title_frame, bg=self.k_title_frame["bg"], fg="White", text="K2", font="Arial 15",
                              anchor=CENTER)
        self.k2_title.pack(fill=BOTH, expand=True, side=LEFT, padx=5)

        # K entry frame
        self.k_entry_frame = Frame(self.task_frame, bg="#001010")
        self.k_entry_frame.pack(fill=X, pady=5)

        # K1 entry
        self.k1_entry = Entry(self.k_entry_frame, font="Arial 15")
        self.k1_entry.pack(fill=X, expand=True, side=LEFT, padx=5)

        # K2 entry
        self.k2_entry = Entry(self.k_entry_frame, font="Arial 15")
        self.k2_entry.pack(fill=X, expand=True, side=LEFT, padx=5)

        # Reverse button
        self.reverse_button = Button(self.task_frame, bg="gray", fg="White", text="Reverse array 3 from K1 to K2",
                                     font="Arial 15",
                                     command=self.on_reverse_button_pressed)
        self.reverse_button.pack(fill=BOTH, expand=True, padx=5, pady=5)

    def start(self):
        """Нажимаем 3 кнопки, чтобы вначале не было пусто, и запускаем окно"""
        self.on_generator_button_pressed(1)
        self.on_generator_button_pressed(2)
        self.on_generator_button_pressed(3)
        self.root.mainloop()

    def change_array(self, array: list, array_number: int):
        """Меняем текст поля массива, соответствующего array_number"""
        if array_number == 1:
            self.array1_field["text"] = str(array).replace("[", "").replace("]", "").replace(", ", " ")
        if array_number == 2:
            self.array2_field["text"] = str(array).replace("[", "").replace("]", "").replace(", ", " ")
        if array_number == 3:
            self.array3_field["text"] = str(array).replace("[", "").replace("]", "").replace(", ", " ")

    @staticmethod
    def show_error(message: str):
        """Показать сообщение об ошибке"""
        messagebox.showerror(title="Error", message=message)

    def on_reverse_button_pressed(self):
        """Проверить k1, k2 на корректность и """
        k1 = str(self.k1_entry.get())
        k2 = str(self.k2_entry.get())

        # Проверка на то, что введены числа
        if not k1.lstrip("-").isdigit() or not k2.lstrip("-").isdigit():
            self.show_error("One of K1 or K2 is invalid")
            return

        # Проверка на то, что k2 >= k1
        k1 = int(k1)
        k2 = int(k2)
        if k2 < k1:
            self.show_error("K1 is greater than K2")
            return

        # Если все ок
        self.presenter.on_reverse_button_pressed(k1, k2)

    def on_generator_button_pressed(self, button_number: int):
        """Выполняем действия после нажатия кнопки, соответствующей button_number"""
        self.presenter.on_generator_button_pressed(button_number)
