full_name = 'John Smith'
age = 20
is_new=True
print(full_name, age, is_new)

print('######################1')

full_name = 'John Smith'
age = str(20)
is_new=True
print(full_name, 'his age is ' + age, is_new)

print('######################2')

name = input('what is your name? ')
favourate_color = input ('what is your favouate color? ')
print (name + ' likes ' + favourate_color)
birth_year = input('Birth year: ')
age = 2019 - int(birth_year)
print (age)

print('######################3')

user_weight_lbs=input('what is your weight? ')
user_weight_lbs = float(user_weight_lbs )
#weight_kg= float(user_weight_lbs)*0.454
weight_kg= user_weight_lbs * 0.454
user_weight_lbs = str(user_weight_lbs)
weight_kg = str(weight_kg)
print(f'Since your weight in LBs is {user_weight_lbs} lbs, then your equivalent weight in KGs is {weight_kg}')

print('######################4')
