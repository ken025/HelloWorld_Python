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

# ----- If Statements -----

# conditions:
# if its a hot day = drink water
# if its a cold day = wear jacket
# otherwise = it is lovely

its_hot = False
its_cold = True

if its_hot:
    print("It is a hot day")
    print("drink Water")
elif its_cold:
    print("It is cold")
    print("wear jacket")
else:
    print("It is lovely")

print("Have a nice day!")


house = 1000000
good_credit = True

if good_credit:
    down = house * 0.1
else:
    down = house * 0.2

print('$', down)

# ------ Logical Operators -----

high_income = True

if high_income and good_credit:
    print("Eligible for Loan")

if high_income or good_credit:
    print("Eligible for Loan")

criminal_record = False

if good_credit and not criminal_record:
    print("Eligible for Loan")

# ----- Comparison Operators -----

temperature = 70

if temperature >= 70:
    print('It is a nice day')
else:
    print("It is cold out")

# username = input("Enter username: ")
# un_count = len(username)
#
# if un_count < 3:
#     print("Must be at least 3 characters!")
# elif un_count > 50:
#     print("Username cannot be over 50 characters")
# else:
#     print("Looks Good!")

# ----- While Loops -----

i = 1

while i <= 5:
    # print(i)
    print('*' * i)
    i = i + 1

print("DONE")


# ----- For Loops -----
for char in 'Python':
    print(char)

for item in ['apples', 'grapes', 'cheese']:
    print(item)

# range object
for num in range(10):
    print(num)

for rng in range(11, 20):
    print(rng)

for step in range(15, 25, 2):
    print(step)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# ----- Nested Loops -----

for x in range(5):
    for y in range(4):
        print(f'({x}, {y})')