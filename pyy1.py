from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
def login():
    if en.get()=='' or ent.get()=='':
        messagebox.showerror('ERROR','FIELDS CANNOT BE EMPTY...')
    elif en.get()=='syed sadik shan ali' and ent.get()=='sad@#shan':
        messagebox.showinfo('SUCCESS','WELCOME HANDSOME BOY...')
        root.destroy()
        import pyy2
        
    else:
        messagebox.showerror('ERROR','PLEASE ENTER CORRECT DETAILS...')
root=Tk()
root.title("STUDENT RESULT MANAGEMENT SYSTEM...")
root.geometry("1350x700+0+0")
root.config(bg="white")
t=Frame(root,bg="orange",bd=10,relief=GROOVE)
t.pack(side=TOP,fill=Y)
la=Label(t,text="STUDENT RESULT MANAGEMENT SYSTEM...",font=("times new roman",30,"bold"),fg="white",bg="black")
la.pack()
image=Image.open("23.jpg")
photo=ImageTk.PhotoImage(image)
l=Label(image=photo,bg="white").place(x=210,y=160,width=1120,height=420)
ur=Label(text="USERNAME:",font=("lucida",19,"bold"))
ur.place(x=555,y=566)
en=Entry(root,font=("times new roman",15,"bold"),fg="royalblue")
en.place(x=720,y=568,width=156,height=30)
pa=Label(text="PASSWORD:",font=("lucida",17,"bold"),fg="red")
pa.place(x=555,y=610)
ent=Entry(root,font=("times new roman",15,"bold"),fg="royalblue")
ent.place(x=720,y=610,width=156,height=30)
bu=Button(root,text="LOGIN",fg="white",bg="blue",pady=7,bd=5,relief=SUNKEN,cursor="hand2",command=login)
bu.place(x=830,y=640,width=112)

root.mainloop()
