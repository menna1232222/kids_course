from tkinter import * 
root=Tk()
root.title("mini calculator")
root.geometry("645x270")
def b1():
     lb["text"]= int(tx1.get("1.0","end"))+int(tx2.get("1.0","end"))
def b2():
     lb["text"]= int(tx1.get("1.0","end"))-int(tx2.get("1.0","end"))
def b3():
     lb["text"]= int(tx1.get("1.0","end"))*int(tx2.get("1.0","end"))
def b4():
     lb["text"]= int(tx1.get("1.0","end"))/int(tx2.get("1.0","end"))
#******************SESSION 1*******************************************************
f1=Frame(root,height=100,width=100,bg="#68228B", pady=15)
tx1=Text(f1,height=4,width=40,bg="#DDA0DD")
tx2=Text(f1,height=4,width=40,bg="#DDA0DD")
b4=Button(f1,text="/",command=b4,height=3,width=15,bg="#FAEBD7")
b1=Button(f1,text="+",command=b1,height=3,width=15,bg="#FAEBD7")
b2=Button(f1,text="-",command=b2,height=3,width=15,bg="#FAEBD7")
b3=Button(f1,text="X",command=b3,height=3,width=15,bg="#FAEBD7")
lb=Label(f1,height=4,width=20)
f1.grid(column=1,row=1)
tx1.grid(column=1,row=1)
tx2.grid(column=2,row=1)
b1.grid(column=1,row=2)
b2.grid(column=2,row=2)
b3.grid(column=1,row=3)
b4.grid(column=2,row=3)
lb.grid(row=4,column=1)
root.mainloop()
