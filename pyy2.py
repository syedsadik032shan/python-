from tkinter import*
from tkinter import ttk,messagebox,filedialog
import time
import pymysql
import pandas
def exi():
    result=messagebox.askyesno("confirm","do you want to exit....")
    if result:
        window.destroy()
    else:
        pass



def export():
    url=filedialog.asksaveasfilename(defaultextension=' .CSV')
    index=st.get_children()
    nl=[]
    for i in index:
        content=st.item(index)
        gg=content['values']
        nl.append(gg)
    table=pandas.DataFrame(nl,columns=["ID","ROLL NO.","NAME","MOBILE NO.","EMAIL","ADDRESS","GENDER","D.O.B"])
    table.to_csv(url,index=False)
    messagebox.showinfo("susses","data is saved....")




def us():
    def upp():
        query="update student set rollno=%s,name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s where id=%s"
        my.execute(query,(rle.get(),nae.get,mbe.get(),ee.get(),ae.get(),ge.get(),de.get(),ide.get()))
        con.commit()
        messagebox.showinfo("susses",f'{ide.get()} is modified sussesfully')
    
        show()
    
    
    
    
    usw=Toplevel()
    usw.resizable(False,False)
    usw.grab_set()
    
    
    
    il=Label(usw,text="ID:",font=("times new roman",20,"bold"),fg="red4")
    il.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    ide=Entry(usw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    ide.grid(row=0,column=1,padx=10,pady=15)

    rl=Label(usw,text="ROLL NO. :",font=("times new roman",20,"bold"),fg="red4") 
    rl.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    rle=Entry(usw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    rle.grid(row=1,column=1,padx=10,pady=15)

    na=Label(usw,text="NAME :",font=("times new roman",20,"bold"),fg="red4")
    na.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    nae=Entry(usw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    nae.grid(row=2,column=1,padx=10,pady=15)

    mb=Label(usw,text="MOBILE NO. :",font=("times new roman",20,"bold"),fg="red4")
    mb.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    mbe=Entry(usw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    mbe.grid(row=3,column=1,padx=10,pady=15)

    e=Label(usw,text="EMAIL ADDRESS :",font=("times new roman",20,"bold"),fg="red4")
    e.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    ee=Entry(usw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    ee.grid(row=4,column=1,padx=10,pady=15)

    a=Label(usw,text="ADDRESS :",font=("times new roman",20,"bold"),fg="red4")
    a.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    ae=Entry(usw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    ae.grid(row=5,column=1,padx=10,pady=15)

    g=Label(usw,text="GENDER :",font=("times new roman",20,"bold"),fg="red4")
    g.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    ge=Entry(usw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    ge.grid(row=6,column=1,padx=10,pady=15)

    dob=Label(usw,text="D.O.B :",font=("times new roman",20,"bold"),fg="red4")
    dob.grid(row=7,column=0,padx=30,pady=15,sticky=W)
    de=Entry(usw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    de.grid(row=7,column=1,padx=10,pady=15)

    aub=Button(usw,text="UPDATE STUDENT",font=("lucida",12,"bold"),bg="royal blue",bd=5,relief=RAISED,cursor="hand2",command=upp)
    aub.grid(row=8,columnspan=2)

    index=st.focus()
    print(index)
    content=st.item(index)
    ld=content['values']
    ide.insert(0,ld[0])
    rle.insert(0,ld[1])
    nae.insert(0,ld[2])
    mbe.insert(0,ld[3])
    ee.insert(0,ld[4])
    ae.insert(0,ld[5])
    ge.insert(0,ld[6])
    de.insert(0,ld[7])
    
    

def show():
    query="select * from student"
    my.execute(query)
    fetch=my.fetchall()
    st.delete(*st.get_children())
    for data in fetch:
            st.insert('',END,values=data)






def ds():
    index=st.focus()
    print(index)
    content=st.item(index)
    contentid=content['values'][0]
    query="delete from student where id=%s"
    my.execute(query,contentid)
    con.commit()
    messagebox.showinfo("susses" ,'f ID {contentid} sussesfully')
    query="select * from student"
    my.execute(query)
    fetch=my.fetchall()
    st.delete(*st.get_children())
    for data in fetch:
        st.insert('',END,values=data)
    
def search():
    def sd():
        query="select * from student where id=%s"
        my.execute(query,(ide.get()))
        fetch=my.fetchall()
        for data in fetch:
            st.insert('',END,values=data)



    sw=Toplevel()
    sw.resizable(False,False)
    sw.grab_set()
    il=Label(sw,text="ID:",font=("times new roman",20,"bold"),fg="red4")
    il.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    ide=Entry(sw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    ide.grid(row=0,column=1,padx=10,pady=15)
    
    
    sb=Button(sw,text="SEARCH STUDENT",font=("lucida",12,"bold"),bg="royal blue",bd=5,relief=RAISED,cursor="hand2",command=sd)
    sb.grid(row=8,columnspan=2)








def add():
    def ads():
        if ide.get()=='' or rle.get()=='' or nae.get()=='' or mbe.get()=='' or ee.get()=='' or ae.get()=='' or ge.get()=='' or de.get()=='' :
            messagebox.showerror("ERROR","ALL FEILDS REQURIED")
        else:
            try:
                query="insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)"
                my.execute(query,(ide.get(),rle.get(),nae.get(),mbe.get(),ee.get(),ae.get(),ge.get(),de.get()))
                con.commit()
                r=messagebox.askyesno("confirm","data add sussesfully")
                if r:
                    ide.delete(0,END)
                    rle.delete(0,END)
                    nae.delete(0,END)
                    mbe.delete(0,END)
                    ee.delete(0,END)
                    ae.delete(0,END)
                    ge.delete(0,END)
                    de.delete(0,END)
                else:
                    pass
            except:
                messagebox.showerror("error","id not reapeated")
                return
            query="select * from student"
            my.execute(query)
            fetch=my.fetchall()
            st.delete(*st.get_children())
            for i in fetch:
                di=list(i)
                st.insert('',END,values=di)

   






    addw=Toplevel()
    addw.resizable(False,False)
    addw.grab_set()
    
    il=Label(addw,text="ID:",font=("times new roman",20,"bold"),fg="red4")
    il.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    ide=Entry(addw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    ide.grid(row=0,column=1,padx=10,pady=15)

    rl=Label(addw,text="ROLL NO. :",font=("times new roman",20,"bold"),fg="red4")
    rl.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    rle=Entry(addw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    rle.grid(row=1,column=1,padx=10,pady=15)

    na=Label(addw,text="NAME :",font=("times new roman",20,"bold"),fg="red4")
    na.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    nae=Entry(addw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    nae.grid(row=2,column=1,padx=10,pady=15)

    mb=Label(addw,text="MOBILE NO. :",font=("times new roman",20,"bold"),fg="red4")
    mb.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    mbe=Entry(addw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    mbe.grid(row=3,column=1,padx=10,pady=15)

    e=Label(addw,text="EMAIL ADDRESS :",font=("times new roman",20,"bold"),fg="red4")
    e.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    ee=Entry(addw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    ee.grid(row=4,column=1,padx=10,pady=15)

    a=Label(addw,text="ADDRESS :",font=("times new roman",20,"bold"),fg="red4")
    a.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    ae=Entry(addw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    ae.grid(row=5,column=1,padx=10,pady=15)

    g=Label(addw,text="GENDER :",font=("times new roman",20,"bold"),fg="red4")
    g.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    ge=Entry(addw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    ge.grid(row=6,column=1,padx=10,pady=15)

    dob=Label(addw,text="D.O.B :",font=("times new roman",20,"bold"),fg="red4")
    dob.grid(row=7,column=0,padx=30,pady=15,sticky=W)
    de=Entry(addw,font=("lucida",12,"bold"),bd=9,relief=RIDGE,width=24)
    de.grid(row=7,column=1,padx=10,pady=15)

    adb=Button(addw,text="ADD STUDENT",font=("lucida",12,"bold"),bg="royal blue",bd=5,relief=RAISED,cursor="hand2",command=ads)
    adb.grid(row=8,columnspan=2)





def cd():
    def connect():
        global my,con
        try:
            con=pymysql.connect(host=he.get(),user=he1.get(),password=he2.get())
            my=con.cursor()
           
        except:
            messagebox.showerror("ERROR","INVALID DETAILS")
            return
        try:
            q="create database studentmanagement"
            my.execute(q)
            q="use studentmanagement"
            my.execute(q)
            q="create table student(id integer not null primary key, rollno integer ,name varchar(100),mobile varchar(10),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50))"
            my.execute(q)
        except:
            q="use studentmanagement"
            my.execute(q)
        messagebox.showinfo("SUSSESS","CONNECTED SUSSESSFULLY...")
        cw.destroy()
        ab.config(state=NORMAL)
        ab1.config(state=NORMAL)
        ab2.config(state=NORMAL)
        ab3.config(state=NORMAL)
        ab4.config(state=NORMAL)
        ab5.config(state=NORMAL)
        ab6.config(state=NORMAL)
    cw=Toplevel()
    cw.resizable(False,False)
    cw.grab_set()
    cw.geometry("500x300+700+200")
    cw.title("CONNECTION...")

    hl=Label(cw,text="HOST NAME:",font=("arial",20,"bold"),fg="red4")
    hl.grid(row=0,column=0,padx=10)

    he=Entry(cw,font=("roman",15,"bold"),fg="black",bd=9,relief=GROOVE)
    he.grid(row=0,column=1,padx=20,pady=20)
    
    hU=Label(cw,text="USERNAME:",font=("arial",20,"bold"),fg="red4")
    hU.grid(row=1,column=0,padx=10)
    
    he1=Entry(cw,font=("roman",15,"bold"),fg="black",bd=9,relief=GROOVE)
    he1.grid(row=1,column=1,padx=20,pady=20)

    pa=Label(cw,text="PASSWORD:",font=("arial",20,"bold"),fg="red4")
    pa.grid(row=2,column=0,padx=10)

    he2=Entry(cw,font=("roman",15,"bold"),fg="black",bd=9,relief=GROOVE)
    he2.grid(row=2,column=1,padx=20,pady=20)


    b=Button(cw,text="CONNECT",font=("arial",10,"bold"),bg="royal blue",bd=9,relief=RAISED,cursor="hand2",command=connect)
    b.place(x=180,y=250,width=150,height=35)


def clock():
    date=time.strftime("%d/%m/%Y")
    cutime=time.strftime("%H:%M:%S")
    dt.config(text=f'    DATE: {date}\nTIME: {cutime}')
    dt.after(1000,clock)
window=Tk()
window.geometry("1350x700+0+0")
window.title("STUDENT RESULT MANAGEMENT SYSTEM...")
dt=Label(window,font=("times new roman",15,"bold"),fg="red")
dt.place(x=5,y=5)
clock()

s="STUDENT RESULT MANAGEMENT SYSTEM..."
sl=Label(window,text=s,font=("lucida",25,"bold"),fg="orange",bg="black",bd=9,relief=GROOVE)
sl.place(x=400,y=20)

cb=Button(window,text="CONNECT TO DATABASE",font=("times new roman",10,"bold"),bd=9,relief=RAISED,bg="royal blue",cursor="hand2",command=cd)
cb.place(x=1150,y=0)



lf=Frame(window)
lf.place(x=10,y=95,width=300,height=600)

ab=Button(lf,text="ADD STUDENT",bd=9,relief=RIDGE,width=40,cursor="hand2",command=add)
ab.grid(row=0,column=0,pady=25)

ab1=Button(lf,text="SEARCH STUDENT",bd=9,relief=RIDGE,width=40,cursor="hand2",command=search)
ab1.grid(row=2,column=0,pady=25)

ab2=Button(lf,text="DELETE STUDENT",bd=9,relief=RIDGE,width=40,cursor="hand2",command=ds)
ab2.grid(row=3,column=0,pady=25)

ab3=Button(lf,text="UPDATE STUDENT",bd=9,relief=RIDGE,width=40,cursor="hand2",command=us)
ab3.grid(row=4,column=0,pady=25)

ab4=Button(lf,text="SHOW STUDENT",bd=9,relief=RIDGE,width=40,cursor="hand2",command=show)
ab4.grid(row=5,column=0,pady=25)

ab5=Button(lf,text="EXPORT DATA",bd=9,relief=RIDGE,width=40,cursor="hand2",command=export)
ab5.grid(row=6,column=0,pady=25)

ab6=Button(lf,text="EXIT",bd=9,relief=RIDGE,width=40,cursor="hand2",bg="RED",command=exi)
ab6.grid(row=7,column=0,pady=25)



rf=Frame(window)
rf.place(x=350,y=95,width=980,height=600)


sb=Scrollbar(rf,orient=HORIZONTAL)
sb1=Scrollbar(rf,orient=VERTICAL)




st=ttk.Treeview(rf,columns=("ID","ROLL NO.","NAME","MOBILE NO.","EMAIL","ADDRESS","GENDER","D.O.B"),
                            xscrollcommand=sb.set,yscrollcommand=sb1.set)

sb.config(command=st.xview)
sb1.config(command=st.yview)

sb.pack(side=BOTTOM,fill=X)
sb1.pack(side=RIGHT,fill=Y)

st.pack(fill=BOTH,expand=1)


st.heading("ID",text="ID")
st.heading("ROLL NO.",text="ROLL NO.")
st.heading("NAME",text="NAME")
st.heading("MOBILE NO.",text="MOBILE NO.")
st.heading("EMAIL",text="EMAIL ADDRESS")
st.heading("ADDRESS",text="ADDRESS")
st.heading("GENDER",text="GENDER")
st.heading("D.O.B",text="D.O.B")

st.column("ID",width=300,anchor=CENTER)
st.column("ROLL NO.",width=300,anchor=CENTER)
st.column("NAME",width=300,anchor=CENTER)
st.column("MOBILE NO.",width=300,anchor=CENTER)
st.column("EMAIL",width=300,anchor=CENTER)
st.column("ADDRESS",width=300,anchor=CENTER)
st.column("GENDER",width=300,anchor=CENTER)
st.column("D.O.B",width=300,anchor=CENTER)

st.config(show="headings")






window.mainloop()