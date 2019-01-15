# should_continue = True
# if should_continue:
#     print('Hello')

# known_people = ['John', 'Anna', 'Mary']

# person = input('Enter the person you know: ')

# if person in known_people:
#     print('You know {}'.format(person))
# else:
#     print('You don\'t know {}'.format(person))

# Exercise


def who_do_you_know():
    people = input('Enter a list of people you know seperated by commas: ')
    people_list = people.split(',')

    people_without_spaces = []
    for person in people_list:
        people_without_spaces.append(person.strip())

    return people_without_spaces


def ask_user():
    name = input('Enter a name: ')
    if name in who_do_you_know():
        print('You know {}'.format(name))
    else:
        print('You do not know {}'.format(name))


ask_user()
