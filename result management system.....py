import mysql.connector as ms
x= ms.connect(host='localhost',user='root',password='syedshan',database='marksheet')
y= x.cursor()
while True:
    ch1=input("I or i if you insert data:")
    if ch1 not in 'Ii':
        break
    
    while True:
        sno=int(input("enter sequence:"))
        rollno=int(input("enter rollno:"))
        name=input("enter name:")
        english=int(input("enter eng marks:"))
        hindi=int(input("enter hindi marks:"))
        cs=int(input("enter cs marks:"))
        maths=int(input("enter maths marks:"))
        biology=int(input("enter biology marks:"))
        physics=int(input("enter physics marks:"))
        chemistry=int(input("enter chemistry marks:"))
        phy_edu=int(input("enter phy_edu marks:"))
        z=(english+hindi+cs+maths+biology+physics+chemistry)
        print(z)
        total=z
        percentage=float(z/500)*100
        query='''
                 insert into student values({},{},'{}',{},{},{},{},{},{},{},{},{},'{}')'''.format(sno,rollno,name,english,hindi,cs,maths,biology,physics,chemistry,phy_edu,total,percentage)
        y.execute(query)

                
        ch=input("Y or y if you add more data:")
        if ch not in 'Yy':
            break
        
while True:
    ch2=input("U or u if you update data:")
    if ch2 not in 'Uu':
        break
    while True:
        ch3=input("N or n if you update name:")
        if ch3 not in 'Nn':
            break
       
        r=int(input("enter rollno. for update data:"))
        name=input("enter name for update:")
    
        q='''
        update student set name='{}' where rollno={}'''.format(name,r) 
        y.execute(q)
    while True:
        ch4=input("M or m if you update marks:")
        if ch4 not in 'Mm':
            break
       
        r=int(input("enter rollno. for update data:"))
        mark=input("enter subject for update:")
        updmarks=int(input("enter updated marks of subject:"))
    
        q='''
        update student set {}={} where rollno={}'''.format(mark,updmarks,r) 
        y.execute(q)
        
while True:
    ch=input("D or d if you wants to delete data:")
    if ch not in 'Dd':
        break
    r=int(input("enter rollno. for update data:"))
    q='''
        delete from student where rollno={}'''.format(r) 
    y.execute(q)
x.commit()

query='''
    select * from student'''
y.execute(query)
t=input("you wants to fetch all data enter 'yes',fetch one by one enter 'one',fetch in range enter 'rr':")
if(t=='yes'):
    r=y.fetchall()
    for i in r:
        print(i)
elif(t=='one'):
    n=int(input("how many data:"))
    for i in range(n):
        s=input("enter press:")
        
        r=y.fetchone()
        print(r)


else:
    n=int(input("how many data:"))
    r=y.fetchmany(n)
    for i in r:
        print(i)
