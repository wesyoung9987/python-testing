def my_method(arg1, arg2):
    return arg1 + arg2


my_method(5, 6)


def my_long_method(arg1, arg2, arg3, arg4, arg5, arg6):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6


my_long_method(1, 2, 3, 4, 5, 6)


def my_list_addition(list_arg):
    return sum(list_arg)


my_list_addition([1, 2, 3, 4, 5, 6])


def addition_simplified(*args):
    # args will be converted to a tuple
    return sum(args)


addition_simplified(1, 2, 3, 4, 5, 6)

##


def named_arguments(arg1, name, location):
    print(arg1)
    print(name)
    print(location)


# order of named args does not matter
# if there are named arguments and non named arguments,
# the named arguments have to go at the end
named_arguments(56, location='UK', name='John')


def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


what_are_kwargs(12, 34, 56, name='Jose', location='UK')
