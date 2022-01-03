from tkinter import *

import requests


class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='id')
        self.lbl2=Label(win, text='name')
        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Subtract')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1=Button(win, text='register', command=self.register)
        self.b1.place(x=100, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
    def register(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        data = {"id": 2}
        r = requests.post("http://127.0.0.1:5000/login", json=data, headers={'Content-Type': 'application/json',"Connection":"keep-alive"})
        self.t3.insert(END, str(r.json()))


window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()