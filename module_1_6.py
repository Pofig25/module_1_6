my_dict = {'Dima':1971, 'Anna':1978, 'Vika':1991}
print('Dict: ',my_dict)
print('Existing value: ', my_dict['Anna'])
print('Not existing value: ', my_dict.get('Misha'))
my_dict.update({'Sasha': 1965, 'Misha': 1995})
a = my_dict.pop('Dima')
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict.items())

my_set = {1, 2, 2, 3, 4, 1, True, 'Яблоко', True}
print('Set: ', set(my_set))
my_set.update([5, 'Банан'])
print('Modified set: ', my_set)