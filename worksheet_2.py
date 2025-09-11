#Tut2
# Q1: 

L = [11, 12, 13, 14]

# (i)
L.append(50)
L.append(60)
print(L)

# (ii)
L.remove(11)
L.remove(13)
print(L)

# (iii)
L.sort()
print("Ascending:", L)

# (iv)
L.sort(reverse=True)
print("Descending:", L)

# (v)
print("13 in list?", 13 in L)

# (vi)
print("Number of elements:", len(L))

# (vii) 
total = 0
for i in L:
    total += i
print("Sum of all:", total)

# (viii) 
odd_sum = 0
for i in L:
    if i % 2 != 0:
        odd_sum += i
print("Sum of odd:", odd_sum)

# (ix) 
even_sum = 0
for i in L:
    if i % 2 == 0:
        even_sum += i
print("Sum of even:", even_sum)

# (x) 
def is_prime(n):
    if n < 2:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

prime_sum = 0
for i in L:
    if is_prime(i):
        prime_sum += i
print("Sum of prime:", prime_sum)

# (xi) 
L.clear()
print("After clear:", L)

# (xii)
del L



# Q2: 

nums = [1, 2, 3, 4]
s = 0
for i in nums:
    s += i
print("Sum is:", s)



# Q3:

nums = [1, 2, 3, 4]
m = 1
for i in nums:
    m *= i
print("Multiply is:", m)



# Q4: 3D array

array3d = []

for i in range(3):
    layer = []
    for j in range(4):
        row = []
        for k in range(6):
            row.append("*")
        layer.append(row)
    array3d.append(layer)

print("Generated 3D Array:", array3d)


# Q5:
D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}

# (i) Add entry
D[8] = 8.8
print(D)

# (ii) Remove key=2
del D[2]
print(D)

# (iii) Check key=6
print("6 in D?", 6 in D)

# (iv) Count elements
print("Count:", len(D))

# (v) Add all values
value_sum = 0
for v in D.values():
    value_sum += v
print("Sum of values:", value_sum)

# (vi) Update key 3
D[3] = 7.1
print(D)

# (vii) Clear dictionary
D.clear()
print(D)



# Q6: 

S1 = {10,20,30,40,50,60}
S2 = {40,50,60,70,80,90}

S1.add(55)
S1.add(66)
print("After add:", S1)

S1.remove(10)
S1.remove(30)
print("After remove:", S1)

print("40 in S1?", 40 in S1)

print("Union:", S1 | S2)
print("Intersection:", S1 & S2)
print("S1 - S2:", S1 - S2)



# Q7.1

import random, string

for i in range(5):  
    length = random.randint(6, 8)
    s = ""
    for j in range(length):
        s += random.choice(string.ascii_letters)
    print(s)

# Q7.2 Primes between 600 and 800
for i in range(600, 801):
    if is_prime(i):
        print(i, end=" ")
print()

# Q7.3 Divisible by 7 and 9
for i in range(100, 1001):
    if i % 7 == 0 and i % 9 == 0:
        print(i, end=" ")
print()



# Q8: Exam schedule

exam_st_date = (11, 12, 2025)
print("The examination will start from: %i / %i / %i" % exam_st_date)

# Q9: Divisible by 5

numbers = [10, 23, 45, 66, 75]
for n in numbers:
    if n % 5 == 0:
        print(n)


# Q10: Even or Odd

num = 7
is_even = (num % 2 == 0)
if is_even:
    print("Even")
else:
    print("Odd")


# Q11: Count substring

text = "Emma is good. Emma likes coding. Emma is smart."
print("Emma count:", text.count("Emma"))


# Q12: New list from 2 lists

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
new_list = []
for i in list1:
    if i % 2 != 0:
        new_list.append(i)
for j in list2:
    if j % 2 == 0:
        new_list.append(j)
print("New list:", new_list)


# Q13: Robot positions
positions = [(2,3),(4,5),(6,7),(7,8)]
for x,y in positions:
    if x % 2 == 0:
        print((x,y))


# Q14: Sensor data

sensor_data = {1:2.3, 2:4.5, 3:1.8, 4:3.6}
for key,val in sensor_data.items():
    if val > 3.0:
        print("Sensor", key, ":", val)


# Q15: Commands

commands_received = {"MOVE","TURN_LEFT","TURN_RIGHT","STOP"}
commands_executed = {"MOVE","TURN_LEFT","STOP"}
print("Not executed:", commands_received - commands_executed)