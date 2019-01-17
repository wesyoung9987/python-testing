def methodception(another):
    return another()


def add_two_numbers():
    return 35 + 77


# print(methodception(add_two_numbers))

# lambda functions don't have a name and can only be one line
print(methodception(lambda: 35 + 77))

my_list = [13, 56, 77, 84]


def not_thirteen(x):
    return x != 13


print(list(filter(not_thirteen, my_list)))

print(list(filter(lambda x: x != 13, my_list)))

print([x for x in my_list if x != 13])
