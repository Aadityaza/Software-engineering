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
        p_balance=cust[x[1]].balance
        if x[3]=='w':
            cust[x[1]].balance= float(cust[x[1]].balance)-float(x[4])
            print(cust[x[1]].name,emp[x[2]].name ,cust[x[1]].balance, p_balance)
        elif x[3]=='d':
            cust[x[1]].balance= float(cust[x[1]].balance)+float(x[4])
            print(cust[x[1]].name,emp[x[2]].name ,cust[x[1]].balance, p_balance)



#print(emp['5'].name)

