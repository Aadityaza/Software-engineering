class Employee:
    id = None
    name="Unknown"

class Customer:
    id=None
    name="Unknown"
    balance =0

with open("data.txt",'r') as file:
  data=file.readlines()


for dat in data:
    x = dat.split(" ")
    custArray=[]
    size_custArray=0
    empArray=[]
    size_empArray=0

    if (dat.startswith('c')):
        custArray.append(Customer())
        custArray[size_custArray].id=x[1]
        custArray[size_custArray].name=x[2]
        custArray[size_custArray].balance=x[3]
        size_custArray+=1
        
    elif (dat.startswith('e')):
        empArray.append(Employee())
        empArray[size_empArray].id=x[1]
        empArray[size_empArray].name=x[2]
        size_empArray+=1
print(empArray[0])

