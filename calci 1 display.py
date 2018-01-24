from tkinter import *
calc=Tk()
x=IntVar()
e=0
z=IntVar()

def answer(t):

    k=z.get()
    answer=float(y.get())
    if t==1:
        answer=answer+float(display.get())
        x.set(0)
        z.set(1)
    elif t==2:
        answer=float(display.get())-answer
        x.set(0)
        z.set(2)
    elif t==3:
        answer=float(display.get())
        x.set(0)
        z.set(3)
    elif t==4:
        answer=float(display.get())
        x.set(0)
        z.set(4)
                   

                   
    elif t==5:
        if k==1:
            answer=answer+float(display.get())
        elif k==2:
            answer=answer-float(display.get())
        elif k==3:
            answer=answer*float(display.get())
        elif k==4:
            answer=answer/float(display.get())
            
        x.set(str(answer))
        answer=0
    y.set(answer)
def renew():
    x.set(0)
    y.set(0)
    z.set(0)
display=Entry(calc,textvariable=x)
x.set(0)
y=IntVar()
display.grid(row=0,column=0,columnspan=3)
b7=Button(calc,text="7",command=lambda: x.set(display.get()+str(7)))
b7.grid(row=1,column=0)
b8=Button(calc,text="8",command=lambda: x.set(display.get()+str(8)))
b8.grid(row=1,column=1)
b9=Button(calc,text="9",command=lambda: x.set(display.get()+str(9)))
b9.grid(row=1,column=2)
b4=Button(calc,text="4",command=lambda: x.set(display.get()+str(4)))
b4.grid(row=2,column=0)
b5=Button(calc,text="5",command=lambda: x.set(display.get()+str(5)))
b5.grid(row=2,column=1)
b6=Button(calc,text="6",command=lambda: x.set(display.get()+str(6)))
b6.grid(row=2,column=2)
b1=Button(calc,text="1",command=lambda: x.set(display.get()+str(1)))
b1.grid(row=3,column=0)
b2=Button(calc,text="2",command=lambda: x.set(display.get()+str(2)))
b2.grid(row=3,column=1)
b3=Button(calc,text="3",command=lambda: x.set(display.get()+str(3)))
b3.grid(row=3,column=2)
b0=Button(calc,text="0",command=lambda: x.set(display.get()+str(0)))
b0.grid(row=4,column=0)
bdot=Button(calc,text=".",command=lambda: x.set(display.get()+"."))
bdot.grid(row=4,column=1)
beq=Button(calc,text="=",command=lambda:answer(5))
beq.grid(row=4,column=2)
badd=Button(calc,text="+",command=lambda:answer(1))
badd.grid(row=1,column=3,rowspan=2)
bsub=Button(calc,text="-",command=lambda:answer(2))
bsub.grid(row=1,column=4,rowspan=2)
bdiv=Button(calc,text="/",command=lambda:answer(4))
bdiv.grid(row=3,column=3,rowspan=2)
bmul=Button(calc,text="x",command=lambda:answer(3))
bmul.grid(row=3,column=4,rowspan=2)

bc=Button(calc,text="c",command=renew)
bc.grid(row=5,column=1)
calc.mainloop()
