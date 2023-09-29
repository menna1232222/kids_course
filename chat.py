from tkinter import * 
root=Tk()
root.geometry("500x240")
root.title("chat")
#----------------------------------------------------------------------------------
def b1 ():
    name =t1.get("1.0","end")
    x=name.find(" ")
    newname=name[0:x]
    lb2['text']="hello , " + newname +" are you happy with me ?"
#//////////////////////////////////////////////////////////////////
def yes ():
    lb3['text']="im very happy to hear that thank you"
#/////////////////////////////////////////////////////////////////
def no ():
    lb3['text']="im very sad to hear "
#---------------------------------------------------------------------------------------

f1=Frame(root,bg="#FAEBD7",pady=10, padx=10)

lb1=Label(f1,height=3,width=30,bg="pink",text="hi im alix robet what is your name ?")

t1=Text(f1,height=2,width=25,bg="#BFEFFF")

b1=Button(f1,command=b1,height=1,width=8,bg="blue",text="push me")

lb2=Label(f1,height=3,width=30,bg="pink")

r1=Radiobutton(f1,command=yes,text="yes",value=1,bg="#BFEFFF")

r2=Radiobutton(f1,command=no,text="no",value=2,bg="#BFEFFF")

lb3=Label(f1,height=3,width=30,bg="pink")

#-------------------------------------------------------------------------------
f1.grid()
lb1.grid(column=1,row=1)
b1.grid(column=2,row=2)
t1.grid(column=3,row=2)
lb2.grid(column=1,row=3)
r1.grid(column=2,row=4)
r2.grid(column=3,row=4)
lb3.grid(column=1,row=5)
#------------------------------------------------------------------------------------------
root.mainloop()