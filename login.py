import tkinter as tk
import os
import time
f = "username"
g = "password"
n = 0

root = tk.Tk()


def a():
    d = k.get()
    e = l.get()
    if d == f:
        if e == g:
            os.startfile("https://www.google.com")
        else:
            m = tk.Label(root, text="Incorret password", foreground='red')
            m.place(x=0, y=100)
    else:
        m = tk.Label(root, text="Incorret username", foreground='red')
        m.place(x=0, y=100)


b = tk.Label(root, text="username")
h = b.place(x=0, y=0)



tk.Label(text="password")

c = tk.Label(root, text='Password')
i = c.place(x=0, y=30)

k = tk.Entry(root, width=20)
k.place(x=75, y=0)
l = tk.Entry(root, width=20, show='*')
l.place(x=75, y=30)

j = tk.Button(root,text='OK',command=a)
j.place(x=100, y=60)
tk.Entry()

root.mainloop()
