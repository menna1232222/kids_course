from tkinter import * 
root=Tk()
root.geometry("500x160")
root.title("chat")
def b1 ():
    lb2['text']="hello , " + t1.get("1.0","end") 

f1=Frame(root,bg="#FAEBD7",pady=10, padx=10)
t1=Text(f1,height=2,width=25,bg="#BFEFFF")
b1=Button(f1,command=b1,height=1,width=8,bg="blue",text="push me")
lb1=Label(f1,height=3,width=30,bg="pink",text="hi im alix robet what is your name ?")
lb2=Label(f1,height=3,width=30,bg="pink")
lb1.grid(column=1,row=1)
lb2.grid(column=1,row=3)
b1.grid(column=2,row=2)
t1.grid(column=3,row=2)
f1.grid()
root.mainloop()