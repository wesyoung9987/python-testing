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


anna = Student('Anna', 'MIT')
anna.marks.append(56)
anna.marks.append(71)
print(anna.average())
