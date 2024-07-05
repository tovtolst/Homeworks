my_dict = {'Joker': 1, 'Pinguin': 2, 'Twoface': 3, 'Riddler': 4}
print (my_dict)
print(my_dict.pop('Joker'))
print(my_dict.get('Scarecrow'))
my_dict.update({'RasalGul':5, 'MadHatter':6})
del(my_dict['Twoface'])
print (my_dict.get('Twoface'))
print(my_dict)
my_set = {1,9,5,3,1,9,1,7,'Victory',False,'Victory'}
print(my_set)
my_set.add(17)
my_set.add('Stalin')
my_set.remove(False)
print(my_set)