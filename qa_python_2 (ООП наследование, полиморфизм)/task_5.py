'''
Напиши класс Results. Проинициализируй в нём атрибуты victories, draws, losses через конструктор.
Напиши класс Football, который наследуется от класса Results. Его методы:
number_of_wins(), который должен возвращать запись вида Футбольных побед: 1. Количество побед должно браться из переменной victories.
number_of_draws(), который должен возвращать запись вида Футбольных ничьих: 1. Количество ничьих должно браться из переменной draws.
number_of_losses(), который должен возвращать запись вида Футбольных поражений: 1. Количество поражений возьми из переменной losses.
total_points(), который должен возвращать запись вида Общее количество очков: 5. Количество очков рассчитай формуле: 3*количество побед + количество ничьих.
Напиши класс Hockey, который наследуется от класса Results. Его методы:
number_of_wins(), который должен возвращать запись вида Хоккейных побед: 1. Количество побед метод берёт из переменной victories.
number_of_draws(), который должен возвращать запись вида Хоккейных ничьих: 1. Количество ничьих метод берёт из переменной draws.
number_of_losses(), который должен возвращать запись вида Хоккейных поражений: 1. Количество поражений должно браться из переменной losses.
total_points(), который должен возвращать запись вида Общее количество очков: 5. Количество очков рассчитывается по формуле: 2*количество побед + количество ничьих.
Создай объекты football_team и hockey_team классов Football и Hockey соответственно. В качестве параметров передай (2, 2, 2).
Вызови все методы для объектов football_team и hockey_team. Используй цикл for. Названия методов при этом не должны повторяться для обоих объектов.
'''


class Results:
    def __init__(self,victories,draws,losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

class Football(Results):
    def number_of_wins(self):
        return f"Футбольных побед: {self.victories}"

    def  number_of_draws(self):
        return f"Футбольных ничьих: {self.draws}"

    def number_of_losses(self):
        return f"Футбольных поражений: {self.losses}"

    def total_points(self):

        return f"Общее количество очков: {3 * self.victories + self.draws}"

class Hockey(Results):
    def number_of_wins(self):
        return f"Хоккейных побед: {self.victories}"

    def number_of_draws(self):
        return  f"Хоккейных ничьих: {self.draws}"

    def number_of_losses(self):
        return f"Хоккейных поражений: {self.losses}"

    def total_points(self):
        return f"Общее количество очков: {2 * self.victories + self.draws}"

football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

for team in (football_team,hockey_team):
    print(team.number_of_wins())
    print(team.number_of_draws())
    print(team.number_of_losses())
    print(team.total_points())
