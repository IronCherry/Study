calls = 0
my_str = 'urban university'
check = 'URBAN'
check_2 = 'UrbaN'


# Считает сколько отработало функций
def count_calls():
    global calls
    calls += 1
    print(calls)


def string_info(string):
    count_calls()
    number_string = len(string)
    upper_string = string.upper()
    lower_string = string.lower()

    new_info_string = number_string, upper_string, lower_string
    return tuple(new_info_string)


def is_contains(string, list_to_search):
    count_calls()
    if string in list_to_search:
        print('True')
    else:
        print('False')


info_str = string_info(my_str)
print(info_str)
is_contains(my_str, info_str)  # Подставить check и check_2 вместо первого аргумента, чтобы проверить
