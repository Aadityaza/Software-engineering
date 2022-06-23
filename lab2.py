class Employee:
    id = None
    name="Unknown"

class Customer:
    id=None
    name="Unknown"
    balance =0

with open("data.txt",'r') as file:
  data=file.readlines()

cust={}
emp={}

for dat in data:
    dat=dat.rstrip()
    x = dat.split(" ")

    if (dat.startswith('c')):
        c=Customer()
        c.id=x[1]
        c.name=x[2]
        c.balance=x[3]
        cust[x[1]]=c

    elif (dat.startswith('e')):
        e=Employee()
        e.id=x[1]
        e.name=x[2]
        emp[x[1]]=e


    elif (dat.startswith('t')):
        if x[3]=='w':
            cust[x[1]].balance= float(cust[x[1]].balance)-float(x[4])
            print(cust[x[1]].name,emp[x[2]].name,'-$',x[4] ,'$',round(cust[x[1]].balance,2))
        elif x[3]=='d':
            cust[x[1]].balance= float(cust[x[1]].balance)+float(x[4])
            print(cust[x[1]].name,emp[x[2]].name ,'+$',x[4],'$',round(cust[x[1]].balance,2))


