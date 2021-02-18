print('Kenneth M. Colon')
print('----------------')
print('python executes line by line')

print('*' * 10)

# ------ Declaring Variables -------

# integer
price = 10
print(price)

# float
rating = 4.9
print(rating)

# string
name = 'Ken'
print(name)

# boolean
is_published = False
print(is_published)

# ------ Receiving Input -----

name = input('Enter Your Name: ')
fav_color = input('Enter Your Favorite Color: ')

print(name + ' likes ' + fav_color)

# ----- Type Conversion -----
birth_year = input('Birth Year: ')
print(type(birth_year))

age = 2021 - int(birth_year)
print(age)
print(type(age))


