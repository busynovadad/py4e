s = 'Monty Python'
print(s[0:4])
print(s[1:4])
fruit1 = 'apple'
fruit2 = 'orange'
fruit3 = 'Apple'
fruit4 = 'Orange'

print(fruit1 < fruit2) # true
print(fruit2 < fruit3) # false
print(fruit3 < fruit4) # true
print(fruit4 < fruit1) # true
print(fruit3 < fruit1)
print(fruit1 < fruit3)
print('WHAT?'.lower())

pos = fruit3.find('l')
print(pos)
print('replace:', fruit3.replace('pp', 'zz'))
print('startswith:', fruit4.startswith('A'))

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])


