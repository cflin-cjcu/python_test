# ch32_3.py
from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_line(100,100,500,100)
canvas.create_line(100,125,500,125,width=5)
canvas.create_line(100,150,500,150,width=10,fill='blue')








