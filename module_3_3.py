def print_params(a=1, b='pig', c=True):
    print(a, b, c)

print_params(1,25,5)
print_params(1, 'hi', [1, 2, 3])

values_list2 = [45.73, False]
values_list = [73, 'wtf', False]
values_dict = {'a': 73, 'b': 'yes', 'c': 37}

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list2, 42)
