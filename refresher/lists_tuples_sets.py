# list
grades = [77, 80, 90, 95, 100]

grades.append(62)
grades[2] = 50

print(grades)
print(grades[0])

# tuple - IMMUTABLE
tuple_grades = (77, 80, 90, 95, 100)

tuple_grades = tuple_grades + (100,)

print(tuple_grades)
print(tuple_grades[0])

# set - unique & unordered
set_grades = {77, 80, 90, 100, 100}

set_grades.add(60)
set_grades.remove(90)

print(set_grades)

# Set operations

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

print(your_lottery_numbers.intersection(winning_numbers))
print(your_lottery_numbers.union(winning_numbers))
print({1, 2, 3, 4}.difference({1, 2}))
