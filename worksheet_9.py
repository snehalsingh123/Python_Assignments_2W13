import tkinter as tk
import math

# Ques-1: Robot Control Panel Window
def q1():
    win = tk.Toplevel()
    win.title("Robot Control Panel")
    win.geometry("500x400")
    win.configure(bg="yellow")

# Ques-2: Black Point at (100,100)
def q2():
    win = tk.Toplevel()
    win.title("Q2: Black Point")
    canvas = tk.Canvas(win, width=400, height=400, bg="white")
    canvas.pack()
    canvas.create_oval(98, 98, 102, 102, fill="black", outline="black")

# Ques-3: Robot Path Polyline
def q3():
    win = tk.Toplevel()
    win.title("Q3: Robot Path")
    canvas = tk.Canvas(win, width=400, height=300, bg="white")
    canvas.pack()
    path = [(20,50), (100,120), (180,90), (250,150)]
    canvas.create_line(path, fill="blue", width=3)

# Ques-4: Moving Point Left to Right
def q4():
    win = tk.Toplevel()
    win.title("Q4: Moving Point")
    canvas = tk.Canvas(win, width=500, height=200, bg="white")
    canvas.pack()
    point = canvas.create_oval(10, 95, 20, 105, fill="red")
    def move_point():
        canvas.move(point, 5, 0)
        pos = canvas.coords(point)
        if pos[2] < 500:
            win.after(50, move_point)
    move_point()

# Ques-5: Simple Robot with Body and Wheels
def q5():
    win = tk.Toplevel()
    win.title("Q5: Simple Robot")
    canvas = tk.Canvas(win, width=400, height=300, bg="white")
    canvas.pack()
    canvas.create_rectangle(150, 100, 250, 200, fill="gray", outline="black", width=2)
    canvas.create_oval(160, 190, 190, 220, fill="black")
    canvas.create_oval(210, 190, 240, 220, fill="black")

# Ques-6: Robot with Direction Buttons
def q6():
    win = tk.Toplevel()
    win.title("Q6: Robot Control")
    canvas = tk.Canvas(win, width=400, height=400, bg="white")
    canvas.pack()
    robot = canvas.create_oval(190, 190, 210, 210, fill="blue")
    def move_up():
        canvas.move(robot, 0, -10)
    def move_down():
        canvas.move(robot, 0, 10)
    def move_left():
        canvas.move(robot, -10, 0)
    def move_right():
        canvas.move(robot, 10, 0)
    frame = tk.Frame(win)
    frame.pack()
    tk.Button(frame, text="Up", command=move_up).grid(row=0, column=1)
    tk.Button(frame, text="Left", command=move_left).grid(row=1, column=0)
    tk.Button(frame, text="Right", command=move_right).grid(row=1, column=2)
    tk.Button(frame, text="Down", command=move_down).grid(row=2, column=1)

# Ques-7: Bouncing Ball
def q7():
    win = tk.Toplevel()
    win.title("Q7: Bouncing Ball")
    WIDTH, HEIGHT = 500, 400
    canvas = tk.Canvas(win, width=WIDTH, height=HEIGHT, bg="white")
    canvas.pack()
    x, y, r = 200, 150, 15
    ball = canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")
    velocity = {"dx": 4, "dy": 3}
    def animate():
        canvas.move(ball, velocity["dx"], velocity["dy"])
        pos = canvas.coords(ball)
        if pos[0] <= 0 or pos[2] >= WIDTH:
            velocity["dx"] = -velocity["dx"]
        if pos[1] <= 0 or pos[3] >= HEIGHT:
            velocity["dy"] = -velocity["dy"]
        win.after(20, animate)
    animate()

# Ques-8: Robot Moving Along Straight Line
def q8():
    win = tk.Toplevel()
    win.title("Q8: Robot Moving")
    canvas = tk.Canvas(win, width=500, height=400, bg="white")
    canvas.pack()
    r = 15
    robot = canvas.create_oval(50-r, 200-r, 50+r, 200+r, fill="green")
    pos = {"x": 50}
    def move_robot():
        if pos["x"] < 450:
            canvas.move(robot, 3, 0)
            pos["x"] += 3
            win.after(30, move_robot)
    move_robot()

# Ques-9: Four-Bar Mechanism
def q9():
    win = tk.Toplevel()
    win.title("Q9: Four-Bar Mechanism")
    canvas = tk.Canvas(win, width=600, height=500, bg="white")
    canvas.pack()
    Ax, Ay = 150, 300
    Dx, Dy = 400, 300
    L2, L3, L4 = 120, 150, 130
    theta = math.radians(30)
    Bx = Ax + L2 * math.cos(theta)
    By = Ay - L2 * math.sin(theta)
    BD = math.sqrt((Dx - Bx)**2 + (Dy - By)**2)
    angle_BD = math.atan2(Dy - By, Dx - Bx)
    cos_angle = (BD**2 + L4**2 - L3**2) / (2 * BD * L4)
    cos_angle = max(-1, min(1, cos_angle))
    angle_offset = math.acos(cos_angle)
    angle_DC = angle_BD + angle_offset
    Cx = Dx - L4 * math.cos(angle_DC)
    Cy = Dy - L4 * math.sin(angle_DC)
    canvas.create_line(Ax, Ay, Dx, Dy, fill="brown", width=4)
    canvas.create_line(Ax, Ay, Bx, By, fill="red", width=4)
    canvas.create_line(Bx, By, Cx, Cy, fill="blue", width=4)
    canvas.create_line(Cx, Cy, Dx, Dy, fill="green", width=4)
    for point, name in [((Ax, Ay), "A"), ((Bx, By), "B"), ((Cx, Cy), "C"), ((Dx, Dy), "D")]:
        canvas.create_oval(point[0]-5, point[1]-5, point[0]+5, point[1]+5, fill="black")
        canvas.create_text(point[0], point[1]-15, text=name, font=("Arial", 12, "bold"))

# Ques-10: Robot with Arrow Keys and Path Trail
def q10():
    win = tk.Toplevel()
    win.title("Q10: Robot with Path")
    canvas = tk.Canvas(win, width=500, height=400, bg="white")
    canvas.pack()
    r = 10
    state = {"x": 250, "y": 200}
    robot = canvas.create_oval(state["x"]-r, state["y"]-r, state["x"]+r, state["y"]+r, fill="blue")
    path_lines = []
    def move(event):
        old_x, old_y = state["x"], state["y"]
        if event.keysym == "Up":
            state["y"] -= 5
        elif event.keysym == "Down":
            state["y"] += 5
        elif event.keysym == "Left":
            state["x"] -= 5
        elif event.keysym == "Right":
            state["x"] += 5
        canvas.coords(robot, state["x"]-r, state["y"]-r, state["x"]+r, state["y"]+r)
        line = canvas.create_line(old_x, old_y, state["x"], state["y"], fill="red", width=2)
        path_lines.append(line)
    def reset():
        for line in path_lines:
            canvas.delete(line)
        path_lines.clear()
        state["x"], state["y"] = 250, 200
        canvas.coords(robot, state["x"]-r, state["y"]-r, state["x"]+r, state["y"]+r)
    win.bind("<Up>", move)
    win.bind("<Down>", move)
    win.bind("<Left>", move)
    win.bind("<Right>", move)
    tk.Button(win, text="RESET", command=reset).pack()
    win.focus_set()

root = tk.Tk()
root.title("Tkinter Worksheet - All Questions")
root.geometry("400x500")
root.configure(bg="#2c3e50")

tk.Label(root, text="Tkinter Worksheet", font=("Arial", 20, "bold"), bg="#2c3e50", fg="white").pack(pady=20)

tk.Button(root, text="Q1: Robot Control Panel", width=30, command=q1).pack(pady=5)
tk.Button(root, text="Q2: Black Point", width=30, command=q2).pack(pady=5)
tk.Button(root, text="Q3: Robot Path Polyline", width=30, command=q3).pack(pady=5)
tk.Button(root, text="Q4: Moving Point", width=30, command=q4).pack(pady=5)
tk.Button(root, text="Q5: Simple Robot", width=30, command=q5).pack(pady=5)
tk.Button(root, text="Q6: Robot with Buttons", width=30, command=q6).pack(pady=5)
tk.Button(root, text="Q7: Bouncing Ball", width=30, command=q7).pack(pady=5)
tk.Button(root, text="Q8: Robot Moving Line", width=30, command=q8).pack(pady=5)
tk.Button(root, text="Q9: Four-Bar Mechanism", width=30, command=q9).pack(pady=5)
tk.Button(root, text="Q10: Robot Arrow Keys", width=30, command=q10).pack(pady=5)

root.mainloop()
