"""inputs = ['nodejs', 'reactjs', 'vuejs']
print(inputs)

for i in inputs:
    inputs.append(i.upper())

print(inputs)"""


def generateParenthesis(n, Open, close, s, temporary_list):

    if (Open == n and close == n):
        temporary_list.append(s)

    if (Open < n):
        generateParenthesis(n, Open + 1, close, s + "(",temporary_list)

    if (close < Open):
        generateParenthesis(n, Open, close + 1, s + ")", temporary_list)


    return temporary_list
    pass


def generate_combination(n):
    temporary_list = []

    combination_list = generateParenthesis(n, 0, 0, "", temporary_list)

    return combination_list
    pass


combination_number = 3

combination_list = generate_combination(n=combination_number)

print(combination_list)

data = [1, 2, 3]

def incr(x):
    return x + 1

print(list(map(incr, data)))


"""class Developer(object):
  def __init__(self, skills):
    self.skills = skills

  def __add__(self, other):
    skills = self.skills + other.skills
    return Developer(skills)

  def __str__(self):
    return "Skills"

A = Developer('NodeJS')
B = Developer('Python')

print(A)
print()
print(B)"""

array = ['Welcome', 'To', 'Turing']
print("-".join(array))

a = [1, 2, 3, 4]
b = [sum(a[0:x+1]) for x in range(0, len(a))]
print(b)

print()
def listSkills(val, list=[]):
    list.append(val)
    return list

list1 = listSkills('NodeJS')
list2 = listSkills('Java', [])
list3 = listSkills('ReactJS')
print("%s" % list1)
print("%s" % list2)
print("%s" % list3)


print()


class Welcome:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('Welcome to ', self.name)


cw = Welcome('Turing')
cw.say_hello()


print()

alphabets = 'abcd'

for i in range(len(alphabets)):
    alphabets[i].upper()

print(alphabets)



print()


class Developer:

    def __init__(self):
        self.__seniority = 'Junior'
        self.skills = ''

    def display(self):
        print('Welcome to Turing with {seniority} developer with skill {skills}'.format(seniority=self.__seniority,
                                                                                        skills=self.skills))


class NodeJS(Developer):

    def __init__(self):
        super().__init__()
        self.__seniority = 'Senior'
        self.skills = 'NodeJS'


c = NodeJS()
c.display()


print()

print("Welcome to TURING".capitalize())


print()


class Hello:

    def __init__(self, a='Welcome to '):
        self.a = a

    def welcome(self, x):
        print(self.a + x)


h = Hello()
h.welcome('Turing')


print()

t = '%(a)s %(b)s %(c)s'
print(t % dict(a='Welcome', b='to', c='Turing'))


print()

"""x = "abcdef"
i = "a"
while i in x[:-1]:
    #print(i, end=" ")
    pass"""

l = [1, 2, 3, 4, 5]
m = map(lambda x: 2**x, l)
print(list(m))



print()


"""def func1():
    x = 50
    return x

func1()
print(x)"""




print()


def add(c, k):
    c.test = c.test + 1
    k = k + 1


class Plus:
    def __init__(self):
        self.test = 0


def main():
    p = Plus()
    index = 0

    for i in range(0, 25):
        add(p, index)

    print("p.test=", p.test)
    print("index=", index)

main()


print()


x = ['ab', 'cd']


print(list(map(lambda x:len(x),x)))


print()



print(2**(3**2), (2**3)**2, (2**3)**3)
print()


l1 = [1, 2, 3, 4]
l2 = [5, 6, 7]

result = l1 + l2
print(result)

print()

i = 'Welcome'


def welcome(i):
    i = i + ', Welcome to Turing'
    return i


welcome('Developer')
print(i)

print()


z = set('abc')
z.add('san')
z.update(set(['p', 'q']))
print(z)

print()


import re
result = re.findall('Welcome to Turing', 'Welcome', 1)
print(result)


print()


"""Y = [2, 5J, 6]
Y.sort()
print(Y)"""



def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)

f(2)
f(3, [3, 2, 1])
f(3)

print()



f = None
for i in range(5):
    with open("app.log", "w") as f:
        if i > 2:
            break

print(f.closed)


print()


try:
 print("Hello")
except:
 print("An exception occurred")
finally:
 print("World")



print()


skills = ['NodeJS', 'Python', 'ReactJS', 'VueJS']


skills.insert(3,"Java")

print(skills)



print()

array1 = [1, 2, 3, 4, 5]
array2 = array1
array2[0] = 0
print(array1)


print()


print([i.lower() for i in "TURING"])


print()

data = [10, 20, 30, 40, 50]
data.pop()
print(data)
data.pop(2)
print(data)


print()

list1 = [1, 2, 6, 12]
list2 = [12, 6, 2, 1]
print(list1 == list2)
print(set(list1) == set(list2))


print()
d = {40 :"john", 45: "peter"}

print(d)


print()

"""inputs = ['nodejs', 'reactjs', 'vuejs']
print(inputs)

for i in inputs:
    inputs.append(i.upper())

print(inputs)"""

