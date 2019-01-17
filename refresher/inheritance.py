class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    # def friend(self, friend_name):
    #     return Student(friend_name, self.school)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        # cls here refers to the class
        # if friend is called with a Student, cls will refer to Student
        # if friend is called with a WorkingStudent, cls will refer to WorkingStudent
        print(args)
        print(*args)
        return cls(friend_name, origin.school, *args, **kwargs)

##


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


anna = WorkingStudent('Anna', 'Oxford', 20.00, 'Software Developer')
print(anna.salary)

friend = WorkingStudent.friend(
    anna, 'Greg', 17.50, job_title='Software Developer')
print(friend.name)
print(friend.school)
print(friend.salary)
