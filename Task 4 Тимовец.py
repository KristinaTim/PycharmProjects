# 4. Создайте класс на тему животных. Используйте статические и динамические переменные, дочерний
# (1 или более) классов на конкретное животное. Публичные и приватные методы.
# Полиморфизм (одинаковые названия методов info в обоих классах, которые выводят информацию о
# животных, либо о конкретном животном данного класса). Создайте объекты каждого класса и
# обратитесь к каждому методу. Напишите один staticmethod, один classmethod, к которым также
# обратитесь


class Animals:
    emp_count = 0
    def __init__(self, name="NoName", klas='NoKlas', ves='Kg'):
        self.name = name
        self.klas = klas
        self.ves = ves
        Animals.emp_count += 1
    def output(self):
        print('Имя: {}. || Класс животного: {}. || Средний вес: {}кг.'.format(self.name, self.klas, self.ves))
    @staticmethod
    def staticmethod():
        print('В мире животных!')
    @classmethod
    def classmethod(cls):
        print('Классификация животных!')


Animals.staticmethod()
Animals.classmethod()
anim1 = Animals('Медведь', 'Млекопитающий', '270')
anim2 = Animals('Лошадь', 'Млекопитающий', '480')
anim3 = Animals('Кролик', 'Млекопитающий', '8')
anim1.output()
anim2.output()
anim3.output()
anim1 = Animals(input(), input(), input())
print('Всего животных:', Animals.emp_count)

