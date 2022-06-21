#include<iostream>
#include<fstream>
#include<string>

using namespace std;

class Customer{
    char type;
    int id;
    string name;
    double balance;
    public:void disp(){
        cout<<" name: "<<name<<"balance"<<balance;
    }
};

class Employee{
    char type;
    int id;
    string name;
    public:void disp(){
        cout<<" name: "<<name<<"id"<<id;
    }
};
 Read(string path){
   ifstream fin;
   Employee e;
   Customer c;
   fin.open(path,ios::in,ios::binary);
    if(!fin)
        cout<<"file not found"<<endl;
    else{
        fin.read(&c,sizeof(c));
    }
    c.disp();
 }
int main(){
   string file= Read("data.txt");


    Customer c[50];
    Employee e[50];

    
}
