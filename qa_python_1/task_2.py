'''
Задание 2
Исправь класс Tester так, чтобы:
при вызове метода work_hard у экземпляра класса tester_1 печаталось 'tester_1 Можно отдыхать';
при вызове метода work_hard у экземпляра класса tester_2 печаталось 'tester_2 Что ж,
ещё часок поработаю!'.
Вызовы менять не нужно.
'''

class Tester:

    def __init__(sels, name):
        sels.name = name
        sels.deadline = True

    def work_hard(self, deadline=True):
        if deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!'

