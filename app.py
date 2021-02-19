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

# ----- Lists ----

# find the greatest number
numbers = [3, 4, 2, 6, 8, 4]
max = numbers[0]

for nmbr in numbers:
    if nmbr > max:
        max = nmbr
print(max)

# ----- 2D Lists -----

# matrix = rectangular array of numbers
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# accessing an item
print(matrix[0][1])
# iterating
for row in matrix:
    # print(row)
    for item in row:
        print(item)

# ----- List Methods -----
nmb = [5, 10, 15]
nmb.append(20)
nmb.remove(5)
nmb.pop()
print(nmb)
print(nmb.index(10))
print(50 in nmb)

# (index, item)
nmb.insert(2, 10)
print(nmb)
print(nmb.count(10))

nmb.sort()
print(nmb)

nmb.reverse()
print(nmb)

# get back only unique items
nmbers = [2, 4, 4, 5, 3, 5, 6, 1]
uniqs = []

for nmber in nmbers:
    if nmber not in uniqs:
        uniqs.append(nmber)
print(uniqs)

# ----- Tuples -----
# similar to lists but immutable

tupls = (1, 2, 3)
print(tupls.count(1))
print(tupls.index(2))
print(tupls[2])

# ----- Unpacking ------
# works with lists and tuppels

coordinates = (1, 2, 3)
# coordinates[0] * coordinates[1] * coordinates[2]
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

x, y, z = coordinates
print(x, y, z)

# ----- Dictionaries ------
# stores multiple key / value pairs

customer = {
    "name": "Ken",
    "age": 20,
    "is_verified": True
}

print(customer["name"])

# to give it a default value, enter 2nd argument
# and receive 'None' instead of error, use get
print(customer.get('birthdate', 'May 25'))

# add key / value
customer['height'] = "5'8"
print(customer)

# turn digits to strings

# phone_num = input("Phone Number: ")
# digit_mapping = {
#     '1': 'One',
#     '2': 'Two',
#     '3': 'Three',
#     '4': 'Four',
#     '5': 'Five'
# }
#
# output = ''
# for ch in phone_num:
#     output += digit_mapping.get(ch, '!') + " "
# print(output)

# ----- Functions -----

def greet_user():
    print("Hello!")
    print("Welcome aboard!")

greet_user()

# ----- Parameters -----

# def greet_usr(name):
#     name = input('Name: ')
#     print(f'Hello, {name}')
# greet_usr(name)

# keyword arguments
def grt_usr(first_name, last_name):
    print(f'Hello, {first_name} {last_name}')
grt_usr(last_name="Colon", first_name="Ken")

# ----- Return Statement -----

def square(num):
    return num * num
print(square(4))
#     print(num * num)
# square(4)

# ----- Exceptions -----
# exit code: 0 = success

# handling errors
# try:
#     age = int(input('Age: '))
#     print(age)
# except ValueError:
# # type of error that our program may encounter
#     print('Invalid Input')

# ----- Classes -----
class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

# ----- Constructors -----
class Pnt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mve(self):
        print('move')

    def drw(self):
        print('draw')

point = Pnt(10, 20)
print(point.x, point.y)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I'm {self.name}")

me = Person("Ken")
me.talk()

# inheritance
class Animal():
    def __init__(self, breed):
        self.breed = breed

    def greet(self):
        print(f"I am a {self.breed}")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog1 = Dog("Daschund")
dog1.greet()

cat1 = Cat("Siamese")
cat1.greet()

# ----- Importing Modules -----
import converters
print(converters.kg_to_lbs(70))

# more specific
# from converters import lbs_to_kg

# ----- Packages -----
import ecommerce.shipping
ecommerce.shipping.cal_shipping()

from ecommerce.shipping import cal_shipping
cal_shipping()