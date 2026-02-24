from datetime import date


class Worker:
    def __init__(self, full_name="", position="", salary=0, year_of_employment=0):
        """Конструктор по умолчанию (создает пустой объект)."""
        self.full_name = full_name
        self.position = position
        self.salary = salary
        self.year_of_employment = year_of_employment

    @classmethod
    def with_args(cls, surname, position, salary, year_of_employment):
        """Альтернативный конструктор, создающий объект с указанными параметрами."""
        return cls(surname, position, salary, year_of_employment)

    def __del__(self):
        """Чисто символический деструктор (нужен по заданию)."""
        pass

    def input_data(self):
        """Метод для ввода данных работника."""
        print("\nВведите данные работника университета \"Синергия\":")
        self.full_name = input("Фамилия и инициалы: ")
        self.position = input("Название занимаемой должности: ")
        while True:
            try:
                self.salary = float(input("Зарплата: "))
                break
            except ValueError:
                print("Некорректный ввод зарплаты.")
        while True:
            try:
                self.year_of_employment = int(input("Год поступления на работу: "))
                break
            except ValueError:
                print("Некорректный ввод года поступления на работу.")

    def display_info(self):
        """Метод для вывода данных о работнике."""
        print(f"\nФамилия и инициалы: {self.full_name}")
        print(f"Должность: {self.position}")
        print(f"Зарплата: {self.salary:.2f}")
        print(f"Год поступления на работу: {self.year_of_employment}")

    def calculate_seniority(self):
        """Метод вычисляющий стаж работника."""
        today = date.today()
        return today.year - self.year_of_employment
