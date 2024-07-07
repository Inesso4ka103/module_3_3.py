def print_params(a = 1, b = 'Hello', c = True):
    print(a, b, c)


print_params()
print_params(2, 18, False)
print_params([1, 2, 3])
print_params(b = 25)
print_params(c = [1,2,3])

values_list = (185, [14, 15,16], 'Привет')
print_params(*values_list)

values_dict = {'a': 'Python', 'b': 456, 'c': [1, 2,3]}
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)