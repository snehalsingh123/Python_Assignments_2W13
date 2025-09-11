# Q1
def diff17(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2
print(diff17(22))
print(diff17(14))

#  Q2
def test_range(n):
    return (n in range(100,1001)) or (n == 2000)
print(test_range(150))
print(test_range(2500))

# Q3
def reverse_string(s):
    return s[::-1]
print(reverse_string("robot"))

# Q4
def count_case(s):
    d = {"UPPER":0, "LOWER":0}
    for c in s:
        if c.isupper():
            d["UPPER"] += 1
        elif c.islower():
            d["LOWER"] += 1
    return d
print(count_case("RoBotics"))

# Q5
def unique_list(lst):
    new = []
    for x in lst:
        if x not in new:
            new.append(x)
    return new
print(unique_list([1,2,2,3,4,4,5]))

# Q6
def even_numbers(lst):
    res = []
    for n in lst:
        if n % 2 == 0:
            res.append(n)
    return res
print(even_numbers([1,2,3,4,5,6,7,8,9]))

# Q7
def robot():
    def move():
        print("Robot is moving")
    move()
robot()

# Q8
def student(name, age, course):
    return name, age, course
print(student.__code__.co_varnames)

# Q9
def move_robot(x, y, direction):
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    return (x,y)
print(move_robot(0,0,"up"))
print(move_robot(2,3,"left"))

# Q10
def classify_temperature(temp):
    if temp < 15:
        return "Cold"
    elif 15 <= temp <= 30:
        return "Moderate"
    else:
        return "Hot"
print(classify_temperature(10))
print(classify_temperature(20))
print(classify_temperature(35))

# Q11
def is_goal_reached(path):
    x = 0
    y = 0
    for move in path:
        if move == "up":
            y += 1
        elif move == "down":
            y -= 1
        elif move == "left":
            x -= 1
        elif move == "right":
            x += 1
    return (x,y) == (2,0)
print(is_goal_reached(["up","right","right","down"]))
print(is_goal_reached(["up","right"]))

# Q12
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
    def display(self):
        print("ID:", self.student_id, "Name:", self.student_name, "Class:", self.student_class)
s = Student(1,"Tanmay","RAI")
s.display()

# Q13
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
student1 = Student(1,"Tanmay","RAI")
student2 = Student(2,"Alice","AI")
print("ID:", student1.student_id, "Name:", student1.student_name, "Class:", student1.student_class)
print("ID:", student2.student_id, "Name:", student2.student_name, "Class:", student2.student_class)

# Q14
import math
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r
    def perimeter(self):
        return 2 * math.pi * self.r
c = Circle(5)
print(c.area())
print(c.perimeter())

# Q15
class StringClass:
    def get_String(self):
        self.s = input("Enter a string: ")
    def print_String(self):
        print(self.s.upper())
obj = StringClass()


# Q16
class Robot:
    def __init__(self, name, task):
        self.name = name
        self.task = task
        self.batterylevel = 100
    def perform_task(self):
        print(self.name, "is performing:", self.task)
        self.batterylevel -= 10
    def recharge(self):
        self.batterylevel = 100
    def status(self):
        print("Name:", self.name, "Task:", self.task, "Battery:", self.batterylevel)
r = Robot("Robo1","Cleaning")
r.perform_task()
r.status()
r.recharge()
r.status()