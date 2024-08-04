'''
С помощью переменной hourly_payment установи почасовой уровень оплаты, равный 400.
Проинициализируй атрибуты name, hours, rest_days, email через конструктор.
Добавь метод класса get_hours(). Если значение hours неизвестно, метод рассчитывает часы, исходя из количества выходных — rest_days. Формула для этого случая такая: (7 - rest_days) * 8.
Добавь метод класса get_email(). Если значение email неизвестно, метод генерирует его так: f"{name}@email.com".
Добавь метод класса set_hourly_payment(). Он меняет значение переменной hourly_payment.
Добавь метод расчёта заработной платы salary(). Формула расчёта такая: hours * hourly_payment.
'''
class EmployeeSalary:
    hourly_payment = 400

    def __init__(self,name,hours,rest_days,email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls,name,hours,rest_days,email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name,hours,rest_days,email)

    @classmethod
    def get_email(cls,name,hours,rest_days,email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name,hours,rest_days,email)

    @classmethod
    def set_hourly_payment(cls,new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment