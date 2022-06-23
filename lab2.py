import filecmp
class Employee:
    id = None
    name="Unknown"

class Customer:
    id=None
    name="Unknown"
    balance =0

def test():
    test_file = open("test.txt", "r")
    output_file = open("output.txt", "r")
    if output_file==test_file:
        pritn('test passed')
    else:
        print("test failed")
    print(filecmp.cmp('test.txt', 'output.txt'))


text_file = open("test.txt", "w")
text_file.close()

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
            output=cust[x[1]].name+' '+emp[x[2]].name+' -$'+x[4] +' $'+' '+str(round(cust[x[1]].balance,2))
            print(output)

            text_file = open("test.txt", "a")
            text_file.write(output+"\n")
        elif x[3]=='d':
            cust[x[1]].balance= float(cust[x[1]].balance)+float(x[4])
            output =cust[x[1]].name+' '+emp[x[2]].name+' +$'+x[4] +' $'+' '+str(round(cust[x[1]].balance,2))
            print(output)
            text_file = open("test.txt", "a")
            text_file.write(output+"\n")

test()
