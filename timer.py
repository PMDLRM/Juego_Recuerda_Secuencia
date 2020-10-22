import turtle
import tkinter as TK

t = turtle.Pen()
for x in range(100):
    t.forward(x)
    t.left(90)

TK.mainloop()