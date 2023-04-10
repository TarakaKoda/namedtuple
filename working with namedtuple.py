from collections import namedtuple

Color = namedtuple("Color", ["mango", "apple", "orange"])
color = Color("yellow", "red", "orange")
size = Color("medium","small","very small")
print(size.apple)

Student = namedtuple("Student", ["srinu", "pavan", "sai", "laku"])
roll_number = Student(5057, 5019, 5013, 5055)
branch = Student("mecs", "ecm", "mpc", "csc")
print(branch.sai)
print(roll_number.pavan)

print(roll_number.srinu)