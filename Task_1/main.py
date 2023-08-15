# Calculator using Python
from tkinter import *

# creating a window
root = Tk()
root.geometry('450x375+0+0')
root.title("Calculator")
root.resizable(False, False)
root.configure(bg="black")

# creating binding Functions
equation = ""

def show(value):
    global equation
    equation+=value
    View_field.configure(text=equation)

def clear():
    global equation
    equation = ""
    View_field.configure(text=equation)

def equate():

    global equation
    result = ""
    if(equation != ""):
        try:
            result = eval(equation)
        except:
            result = "Error"
    equation = ""
    View_field.configure(text=result)

# creating buttons to bottom frame
btn_bracket1 = Button( font=('arial', 18, 'bold'), text='(', bd=3, relief='groove',command=lambda: show("("), width=6, bg='black', fg="white")
btn_bracket1.place(x=15, y=75)

btn_bracket2 = Button( font=('arial', 18, 'bold'), text=')', bd=3, relief='groove',command=lambda: show(")"), width=6, bg='black', fg="white")
btn_bracket2.place(x=120, y=75)

btn_perc = Button(font=('arial', 18, 'bold'), text='%', bd=3, relief='groove',command=lambda: show("%"), width=6, bg='black', fg="white")
btn_perc.place(x=225, y=75)

btn_clear = Button(font=('arial', 18, 'bold'), text='C', bd=3, relief='groove',command=lambda: clear(), width=6, bg='blue', fg="White")
btn_clear.place(x=331, y=75)

btn_7 = Button(font=('arial', 18, 'bold'), text='7', bd=3, relief='groove',command=lambda: show("7"), width=6, bg='black', fg="white")
btn_7.place(x=15, y=135)

btn_8 = Button(font=('arial', 18, 'bold'), text='8', bd=3, relief='groove',command=lambda: show("8"), width=6, bg='black', fg="white")
btn_8.place(x=120, y=135)

btn_9 = Button(font=('arial', 18, 'bold'), text='9', bd=3, relief='groove',command=lambda: show("9"), width=6, bg='black', fg="white")
btn_9.place(x=225, y=135)

btn_div = Button(font=('arial', 18, 'bold'), text='/', bd=3, relief='groove',command=lambda: show("/"), width=6, bg='black', fg="white")
btn_div.place(x=331, y=135)

btn_4 = Button(font=('arial', 18, 'bold'), text='4', bd=3, relief='groove',command=lambda: show("4"), width=6, bg='black', fg="white")
btn_4.place(x=15, y=195)

btn_5 = Button(font=('arial', 18, 'bold'), text='5', bd=3, relief='groove',command=lambda: show("5"), width=6, bg='black', fg="white")
btn_5.place(x=120, y=195)

btn_6 = Button(font=('arial', 18, 'bold'), text='6', bd=3, relief='groove',command=lambda: show("6"), width=6, bg='black', fg="white")
btn_6.place(x=225, y=195)

btn_mul = Button(font=('arial', 18, 'bold'), text='x', bd=3, relief='groove', width=6,command=lambda: show("*"), bg='black', fg="white")
btn_mul.place(x=331, y=195)

btn_1 = Button(font=('arial', 18, 'bold'), text='1', bd=3,command=lambda: show("1"), relief='groove', width=6, bg='black', fg="white")
btn_1.place(x=15, y=255)

btn_2 = Button(font=('arial', 18, 'bold'), text='2', bd=3, relief='groove',command=lambda: show("2"), width=6, bg='black', fg="white")
btn_2.place(x=120, y=255)

btn_3 = Button(font=('arial', 18, 'bold'), text='3', bd=3, relief='groove',command=lambda: show("3"), width=6, bg='black', fg="white")
btn_3.place(x=225, y=255)

btn_sub = Button(font=('arial', 18, 'bold'), text='-', bd=3, relief='groove',command=lambda: show("-"), width=6, bg='black', fg="white")
btn_sub.place(x=331, y=255)

btn_0 = Button(font=('arial', 18, 'bold'), text='0', bd=3, relief='groove', command=lambda: show("0"), width=6, bg='black', fg="white")
btn_0.place(x=15, y=315)

btn_decimal = Button(font=('arial', 18, 'bold'), text='.', bd=3, relief='groove',  command=lambda: show("."), width=6, bg='black', fg="white")
btn_decimal.place(x=120, y=315)

btn_equal = Button(font=('arial', 18, 'bold'), text='=', bd=3, relief='groove',command=lambda: equate(), width=6, bg='white', fg="Blue")
btn_equal.place(x=225, y=315)


btn_add = Button(font=('arial', 18, 'bold'), text='+', bd=3, relief='groove', command=lambda: show("+"), width=6, bg='black', fg="white")
btn_add.place(x=331, y=315)

# Adding text feild to top frame
View_field = Label(font=("arial",30), width=18, justify='right', state=NORMAL, bg="white",anchor="e")
View_field.place(x=13, y=15)

# Closing the window
root.mainloop()





