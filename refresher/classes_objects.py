lottery_player = {
    'name': 'Rolf',
    'numbers': (13, 45, 66, 23, 22)
}


class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (13, 45, 66, 23, 22)

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer('Rolf')
player_one.numbers = (1, 2, 3, 4, 5, 6)
player_two = LotteryPlayer('John')
print(player_one.name)
print(player_one.total())

print(player_one.numbers == player_two.numbers)

##


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    # do not need to pass in self
    # can be called with either anna.go_to_school() or Student.go_to_school()
    @staticmethod
    def go_to_school():
        print('I\'m going to school')

    # pass in cls witch refers to the class, not the object
    # can be called with either anna.go_to_school() or Student.go_to_school()
    # and can reference the class by using cls inside of the method
    # @classmethod
    # def go_to_school(cls):
    #     print('I\'m going to school')


anna = Student('Anna', 'MIT')
rolf = Student('Rolf', 'Oxford')
anna.marks.append(56)
anna.marks.append(71)
print(anna.average())
Student.go_to_school()
