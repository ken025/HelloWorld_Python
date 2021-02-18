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

# name = input('Enter Your Name: ')
# fav_color = input('Enter Your Favorite Color: ')
#
# print(name + ' likes ' + fav_color)

# ----- Type Conversion -----
# birth_year = input('Birth Year: ')
# print(type(birth_year))
#
# age = 2021 - int(birth_year)
# print(age)
# print(type(age))

# ----- Strings -----

course = "Python's Course for Beginners"
print(course)

course_2 = 'Python for "Beginners"'
print(course_2)

# grabbing characters
print(course_2[0])
print(course_2[-1])
print(course_2[0:3])
print(course_2[3:])
print(course_2[:5])

# copying string
copy = course_2[:]
print(copy)

# multiple lined strings (triple quotes ''')

greeting = '''
Hello,

I am testing multi-line strings.

Will it work?
'''
print(greeting)

# ----- Formatted Strings ------

first = 'Ken'
last = 'Colon'

# prefix with f
mssg = f'{first} [{last}] is a coder'
print(mssg)

# ------ String Methods -----

# counts characters
print(len(course_2))

# . opperators
print(course.upper())
print(course.find('e'))
print(course.replace('Beginners', 'Mid-Level'))
print('for' in course)
print('For' in course)

# ------ Arithmetic Operators ------

print(10 + 5)
print(10 - 5)
print(10 * 5)

# float
print(10 / 5)

# integer
print(10 // 5)

# modulos (remainder)
print(10 % 5)

#power (squared)
print(10 ** 5)

# ------ Augmented Assignment -----

x = 10
print(x)

x += 5
print(x)

x -= 5
print(x)

# ------ Operator Precedence ------
# PEMDAS
y = (2 + 3) * 10 + 3 * 2 ** 2
print(y)

# ----- Math Functions -----
z = 4.8
print(round(z))

#switch to pos
print(abs(-2.5))

# using dot operators - python 3 math module
import math
print(math.ceil(2.5))
print(math.floor(2.5))


