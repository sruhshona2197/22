
# 46
class Engine:
    def power(self):
        return "500HP"

class Car:
    def __init__(self):
        self.engine = Engine()

c = Car()
print(c.engine.power())


# 47
class Music:
    def play(self):
        return "Playing"

class Piano(Music):
    pass

p = Piano()
print(p.play())


# 48
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly(self):
        return self.salary * 12

e = Employee("John", 2000)
print(e.yearly())


# 49
class Number:
    def __init__(self, n):
        self.n = n

    def __mul__(self, other):
        return self.n * other.n

a = Number(5)
b = Number(6)
print(a * b)


# 50
class Message:
    def __init__(self, text):
        self.text = text

    def __len__(self):
        return len(self.text)

m = Message("Hello")
print(len(m))
