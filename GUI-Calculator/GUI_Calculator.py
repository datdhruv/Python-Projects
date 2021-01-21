import tkinter
window = tkinter.Tk()
expression = tkinter.StringVar()
expression.set("Enter the operation")
label = tkinter.Label(window,textvariable=expression)
label.pack()
frame = tkinter.Frame(window)
frame.pack()


#the controllers
def on_numclick(n:str) -> str:
    global expression
    if expression.get() == "Enter the operation":
        expression.set("")
    expression.set(expression.get() + str(n))
def on_opclick(op:str) -> str:
    global expression
    if op == "+" :
        expression.set(expression.get() + " + ")
    elif op == "-":
        expression.set(expression.get() + " - ")
    elif op == "x":
        expression.set(expression.get() + " x ")
    elif op == "/":
        expression.set(expression.get() + " / ")
    elif op == "=":
        total = eval(expression.get())
        expression.set(str(total))
    elif op == "<":
        expression.set(expression.get()[:-1])
    elif op == "clr":
        expression.set("")

#The views
#button initialization and commands
button0 = tkinter.Button(frame,text=0,command=lambda:on_numclick(0))
button0.grid(row=4,column=2)
button1 = tkinter.Button(frame,text=1,command=lambda: on_numclick(1))
button1.grid(row=1,column=1)
button2 = tkinter.Button(frame,text=2,command=lambda: on_numclick(2))
button2.grid(row=1,column=2)
button3 = tkinter.Button(frame,text=3,command=lambda: on_numclick(3))
button3.grid(row=1,column=3)
button4 = tkinter.Button(frame,text=4,command=lambda: on_numclick(4))
button4.grid(row=2,column=1)
button5 = tkinter.Button(frame,text=5,command=lambda: on_numclick(5))
button5.grid(row=2,column=2)
button6 = tkinter.Button(frame,text=6,command=lambda: on_numclick(6))
button6.grid(row=2,column=3)
button7 = tkinter.Button(frame,text=7,command=lambda: on_numclick(7))
button7.grid(row=3,column=1)
button8 = tkinter.Button(frame,text=8,command=lambda: on_numclick(8))
button8.grid(row=3,column=2)
button9 = tkinter.Button(frame,text=9,command=lambda: on_numclick(9))
button9.grid(row=3,column=3)
add_button = tkinter.Button(frame,text="+",command = lambda: on_opclick("+"))
add_button.grid(row=1,column=4)
sub_button = tkinter.Button(frame,text="-",command = lambda: on_opclick("-"))
sub_button.grid(row=2,column=4)
mult_button = tkinter.Button(frame,text="x",command = lambda: on_opclick("x"))
mult_button.grid(row=3,column=4)
div_button = tkinter.Button(frame,text="/",command = lambda: on_opclick("/"))
div_button.grid(row=4,column=4)
eq_button = tkinter.Button(frame,text="=",command = lambda: on_opclick("="))
eq_button.grid(row=4,column=4)
clr_button = tkinter.Button(frame,text="clr",command = lambda:on_opclick("clr"))
clr_button.grid(row=4,column=1)
back_button = tkinter.Button(frame,text = "<",command = lambda:on_opclick("<"))
back_button.grid(row=4,column=3)




window.mainloop()
