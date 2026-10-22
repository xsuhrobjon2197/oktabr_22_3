#5-misol
class Lamp:
    pass

l1 = Lamp()
l2 = Lamp()
print(l1 is l2)

#6-misol
class User:
    def __init__(self, username, age=18):
        self.username = username
        self.age = age

u1 = User("sara")
u2 = User("bek", 30)
print(u1.username, u1.age)
print(u2.username, u2.age)
