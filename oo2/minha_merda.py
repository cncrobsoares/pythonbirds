my_dict = {
    "1": "a",
    "2": "b",
    "3": "c"
}

my_dict.items()  # dict_items([('1', 'a'), ('3', 'c'), ('2', 'b')])
my_dict.keys()  # dict_keys(['1', '3', '2'])
my_dict.values()  # dict_values(['a', 'c', 'b'])
print(my_dict.items())  # dict_items([('1', 'a'), ('3', 'c'), ('2', 'b')])

v = my_dict.values()
print(my_dict.values(), my_dict.keys())
print(v)
