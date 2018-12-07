'''
LIST COMPREHENSION 
'''

items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = [
    i
    for i in items
    if i % 2 == 0
]
# for i in items:
#     if i % 2 == 0:
#         even.append(i)

print('All even {}'.format(even))

'''
GENERATOR EXPRESSION
'''

users = (
    {'user': 'User1', 'age': 20},
    {'user': 'User2', 'age': 25}
)
dict_of_users = list((
    u['age']
    for u in users
    if int(u['age']) > 20
))
dict_of_digits = {i: i ** 2 for i in range(5)}
# even = [i for i in list if i % 2 == 0]
# for i in list:
#     if i % 2 == 0:
#         even.append(i)

print('Age: {}'.format(dict_of_users))
print(dict_of_digits)
