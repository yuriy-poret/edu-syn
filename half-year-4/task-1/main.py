import datetime


DIGITS = {
    '0': [
        '*****',
        '*   *',
        '*   *',
        '*   *',
        '*****'
    ],
    '1': [
        '  *  ',
        ' **  ',
        '* *  ',
        '  *  ',
        '*****'
    ],
    '2': [
        '*****',
        '    *',
        ' *** ',
        '*    ',
        '*****'
    ],
    '3': [
        '*****',
        '    *',
        ' ****',
        '    *',
        '*****'
    ],
    '4': [
        '*   *',
        '*   *',
        '*****',
        '    *',
        '    *'
    ],
    '5': [
        '*****',
        '*    ',
        '*****',
        '    *',
        '*****'
    ],
    '6': [
        '*****',
        '*    ',
        '*****',
        '*   *',
        '*****'
    ],
    '7': [
        '*****',
        '    *',
        '   * ',
        '  *  ',
        ' *   '
    ],
    '8': [
        ' *** ',
        '*   *',
        ' *** ',
        '*   *',
        ' *** '
    ],
    '9': [
        '*****',
        '*   *',
        '*****',
        '    *',
        '*****'
    ]
}

class BirthdayInfo:
    def __init__(self):
        print('\nВведите числами следующие данные:')
        self.day   = int(input("\nКакого числа Вы родились: "))
        self.month = int(input("Номер месяца в году: "))
        self.year  = int(input("Год рождения (пример: 1980): "))

    def trans_weekday(self, weekday):
        weekdays = {
            'Sunday'   : 'Воскресенье',
            'Monday'   : 'Понедельник',
            'Tuesday'  : 'Вторник',
            'Wednesday': 'Среда',
            'Thursday' : 'Четверг',
            'Friday'   : 'Пятница',
            'Saturday' : 'Суббота',
        }
        return weekdays[str(weekday)]

    def get_weekday(self):
        try:
            date = datetime.date(self.year, self.month, self.day)
            return date.strftime("%A")
        except ValueError:
            return "Некорректная дата"

    def is_leap_year(self):
        year = self.year
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.year - ((today.month, today.day) < (self.month, self.day))
        return age

    def get_age_text(self):
        age             = self.get_age()
        last_digit      = age % 10
        last_two_digits = age % 100

        if 11 <= last_two_digits <= 14:
            return f"{age} лет"
        elif last_digit == 1:
            return f"{age} год"
        elif 2 <= last_digit <= 4:
            return f"{age} года"
        else:
            return f"{age} лет"

    def display_as_stars(self):

        def digit_to_star_lines(k):
            return DIGITS.get(str(k), ['     '] * 5)

        def format_digit(k):
            return f'0{k}' if k < 10 else str(k)

        day_lines   = [digit_to_star_lines(d) for d in format_digit(self.day)]
        month_lines = [digit_to_star_lines(d) for d in format_digit(self.month)]
        year_lines  = [digit_to_star_lines(d) for d in str(self.year)]

        for i in range(5):
            line = ' '.join([y[i] for y in day_lines]) + '   ' + ' '.join([y[i] for y in month_lines]) + '   ' + ' '.join([y[i] for y in year_lines])
            print(line)

if __name__ == "__main__":
    birthday = BirthdayInfo()

    print(f"\nДень недели: {birthday.trans_weekday(birthday.get_weekday())}")
    print(f"Високосный год: {'Да' if birthday.is_leap_year() else 'Нет'}")
    print(f"Вам сейчас: {birthday.get_age_text()}")

    print("\nВаша дата рождения:\n")
    birthday.display_as_stars()
