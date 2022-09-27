# 3. Дописать классы Company, Programmer.
# Тесты:
# 1.Вызовите справку по программированию
# 2.Создайте объекты классов Company, Programmer
# 3.Используя объект класса Programmer, повысьте свой уровень квалификации
# 4.Дойдите до уровня lead

class Company:
    levels={1:'junior',2:'midle',3:'senior',4:'lead'}
    def __init__(self,index):
        if index>4:index=4
        self._index=index
        self._levels=self.levels[self._index]
    def level_up(self):
        if self._index!=4:
            self._index+=1
            self._levels=self.levels[self._index]
            print('Уровень повышен до:',self._levels)
    def s_lead(self):
        if self._index==4:
            print('Достигнут максимальный уровень!')
        else:
            print('Ваш уровень слишком мал!', self.levels[self._index])
            return self._index==4
class Programmer(Company):
    def __init__(self,name,uroven):
        super().__init__(uroven)
        self.name=name
    def work(self):
        self.lever_up()
    @staticmethod
    def knowledge_base():
        print(Company.levels)
artsiom=Programmer('Artem',1)
artsiom.knowledge_base()
while artsiom.s_lead()==False:
    artsiom.level_up()
artsiom.s_lead()



