
import numpy as np
import math

# Question 1
class Points():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def Distance(self):
        return math.sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)
    
    def Midpoint(self):
        mid_x = (self.x1 + self.x2) / 2
        mid_y = (self.y1 + self.y2) / 2
        return (mid_x, mid_y)
    
    def Equation(self):
        if self.x2 == self.x1:
            return "Vertical line"
        m = (self.y2 - self.y1) / (self.x2 - self.x1)
        c = self.y1 - m * self.x1
        return f"y = {m}(x - {self.x1}) + {c}"
    
    def Reflection(self, x3, y3):
        if self.x2 == self.x1:
            xr = 2*self.x1 - x3
            yr = y3
        else:
            m = (self.y2 - self.y1) / (self.x2 - self.x1)
            c = self.y1 - m * self.x1
            d = (x3 + (y3 - c) * m) / (1 + m**2)
            xr = 2*d - x3
            yr = 2*d*m - y3 + 2*c
        return (xr, yr)

points = Points(1, 2, 3, 4)
print("Distance between A and B:", points.Distance())
mid = points.Midpoint()
print("Midpoint of A and B is:", mid[0], ",", mid[1])
print("Equation of line AB is:", points.Equation())
xr, yr = points.Reflection(5, 6)
print("Reflection of point C is:", xr, ",", yr)


# Question 2 
A = np.array([float(x) for x in input("Enter vector A (space separated): ").split()])
B = np.array([float(x) for x in input("Enter vector B (space separated): ").split()])
C = np.array([float(x) for x in input("Enter vector C (space separated): ").split()])

R = A + B + C
print("Vector Addition (A+B+C):", R)

print("Magnitude of A:", np.linalg.norm(A))
print("Magnitude of B:", np.linalg.norm(B))
print("Magnitude of C:", np.linalg.norm(C))

print("Dot product of A and B:", np.dot(A, B))
print("Dot product of B and C:", np.dot(B, C))

def angle_between(u, v):
    return np.degrees(np.arccos(np.dot(u, v)/(np.linalg.norm(u) * np.linalg.norm(v))))

print("Angle between A and B:", angle_between(A, B))
print("Angle between A and C:", angle_between(A, C))
print("Angle between B and C:", angle_between(B, C))

proj = (np.dot(A, B) / np.dot(B, B)) * B
print("Projection of A onto B:", proj)


# Question 3
S = np.array([float(x) for x in input("Start point S (x y): ").split()])
E = np.array([float(x) for x in input("End point E (x y): ").split()])
P = np.array([float(x) for x in input("Point P (x y): ").split()])

seg_len = np.linalg.norm(E - S)
print("Segment Length SE:", seg_len)

t = np.dot(P - S, E - S) / np.dot(E - S, E - S)
t = max(0, min(1, t))
closest = S + t * (E - S)
print("Closest Point on Segment SE to P:", closest[0], closest[1])

dist_to_segment = np.linalg.norm(P - closest)
print("Distance from P to Segment SE:", dist_to_segment)


# Question 4
a1, b1, c1 = map(float, input("Line L1 (a1 b1 c1): ").split())
a2, b2, c2 = map(float, input("Line L2 (a2 b2 c2): ").split())
D = a1*b2 - a2*b1
if D != 0:
    x = (c1*b2 - c2*b1) / D
    y = (a1*c2 - a2*c1) / D
    print("Intersection Point:", x, y)
else:
    print("Lines are parallel or coincident.")


