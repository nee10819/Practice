print("Hello World!!!")

# Integer
# Float
print(1*3)
print (1/2)
print(2 ** 4)
print(4 % 2)
print(5 % 2)

var = 2
print(var)

x = 2
y = 3
print(x + y)
print (x + x)

# Variable name can't be started with special characters or numeric value
12var = 12 # this will error out
$var = 10 # this will error out

name_of_var = 12
print(name_of_var)

# Strings
print('single quote')
print("single quote's")

num = 12
name = "Sam"
print('My name is {} and my number is {}'.format(name, num))
# Sequence of variable matters
print('My name is {} and my number is {}'.format(num, name))
# Sequence of variable doesn't matter
print('My name is {one} and my number is {two}'.format(two = num, one = name))
# Same variable can be reused multiple times
print('My name is {one} and my number is {two}, and more {one}'.format(two = num, one = name))

# indexing in python starts at 0
s = 'hello'
print(s[0])
print(s[4])
print(s[len(s)-1])

s = 'abcdefghijk'
print(s[0])
# Output everything from index 0 till end
print(s[0:])
# Output everything from index 0 till mentioned index -1
print(s[:3])
print(s[0:3])
print(s[3:6])

# list
my_list = ['a', 'b', 'c']
print(my_list)
my_list.append('d')
print(my_list)

print(my_list[1:3])
print(my_list[-1])

my_list[0] = 'NEW'
print(my_list)

nest = [1,2,[3,4]]
print(nest)
print(nest[2])
print(nest[2][1])

nest = [1,2,3,[4,5,['target']]]
print(nest)
print(nest[3])
print(nest[3][2])
print(nest[3][2][0])

# Dictionary
d = {'key1':'value', 'key2':123}
print(d)
print(d[0]) # this will error out
print(d['key1'])
print(d['key2'])

d = {'k1':[1,2,3]}
print(d)
print(d['k1'])
print(d['k1'][0])

my_list = d['k1']
print(my_list)
print(my_list[1])

# Booleans
# True and False

# Tuples
# Tuples are immutable
# We cannot change items in tuples
my_list = [1,2,3]
t = (1,2,3)
print(t)

# Set
# Set is a collection of unique elements
print({1,2,3})
print({1,2,3,1,2,3,1,2,3,4,5,6,4,5,6})

print(set([1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5]))

# Comparision Operators
print(1 > 2)
print(1 < 2)
print(1 == 1)
print(1 >= 2)
print(1 <= 2)
print('hi' == 'bye')

print((1 > 2) and (2>3))
print((1 < 2) and (2>3))
print((1 < 2) and (2<3))
print((1 < 2) or (2>3))

# Conditional
if 1<2:
    print('yep')


if 1 ==2:
    print('First')
else:
    print('last')
    
if 1 == 1:
    print('First')
else:
    print('last')
    
if 1 == 2:
    print('First')
elif 3 == 3:
    print('second')
else:
    print('last')
    

# for loop and while loop
seq = [1,2,3,4,5]
for item in seq:
    print(item)
    
for item in seq:
    print('hello')
    
# while loop
i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1
    

# range()
# range is a generator numerical values
for x in range(0,5):
    print(x)
    
# list comprehension
x = [1,2,3,4]

out = []
for num in x:
    out.append(num**2)
print(out)

out = [num**2 for num in x] # list comprehension
print(out)


# functions
def my_func(param1):
    print(param1)
    
my_func('hello')

def my_func2(name):
    print('Hello ' + name)
    
my_func2('Jose')

def square(num):
    return num**2

output = square(2)
print(output)
square


def times2(var):
    return var*2
times2(5)

# map()
seq = [1,2,3,4,5]

list(map(times2,seq))

# lambda inside map
list(map(lambda num: num*3, seq))

# filter
list(filter(lambda num: num%2 == 0, seq))

# methods
s = 'hello my name is Sam'
s.lower()
s.upper()
s.split()

tweet = 'Go Sports! #Sports'
tweet.split()
tweet.split('#')


d = {'k1': 1, 'k2': 2}
d.keys()
d.values()
d.items()

lst = [1,2,3]
lst.pop()
lst
lst.pop(0)
lst

'x' in [1,2,3]
'x' in ['x','y','z']

# Tuples unpacking
x = [(1,2),(3,4),(5,6)]
x
x[0]
x[0][1]

for item in x:
    print(item)

for a,b in x:
    print(a)
    
for (a,b) in x:
    print(b)
    
for a,b in x:
    print(a)
    print(b)
    





