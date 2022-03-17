class Person:
  def __init__(self, name, age, money):
    self.name = name
    self.age = age
    self.money = money

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Will", 48, 1000)

print(p1.name)
print(p1.age)
print(p1.money)

