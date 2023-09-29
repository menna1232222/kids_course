from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.geometry("610x310")
def act ():
    if list.get(ACTIVE)=="english":
        l1["text"]="Hello, how are you?"
    elif list.get(ACTIVE)=="french":
        l1["text"]="Hey comment allez-vous?"
    elif list.get(ACTIVE)=="italin":
        l1["text"]="Ciao, come stai?"
    elif list.get(ACTIVE)=="arabic":
        l1["text"]="اهلا ,كيف حالك؟"
#------------------------------------------------------------------
f1=Frame(root)
list=Listbox(f1,height=19,bg="#9ACD32")
b1=Button(f1,command=act,text="-->",height=20,bg="#008000",fg="white")
l1=Label(f1,height=17,width=50,bg="#E6DAA6",font=90)
#------------------------------------------------------------
values=["english","french","italin","arabic"]
for i in range (0,len(values)):
    list.insert(i,values[i])
#----------------------------------------------------------
f1.pack()
list.grid(column=1,row=1)
l1.grid(column=3,row=1)
b1.grid(column=2,row=1)
root.mainloop()
    

