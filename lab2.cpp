#include<iostream>
#include<fstream>
#include<string>

using namespace std;

class Customer{
    string name;
    double balance;
};

class Employee{
    string name;
};
string Read(string path){
    fstream newfile;
   
   newfile.open(path,ios::in ); 
   if (newfile.is_open()){   //checking whether the file is open
      string str;
      while(getline(newfile, str)){ 
         cout << str << "\n"; 
      }
      newfile.close();  
   }
   
}
int main(){
   string file= Read("data.txt");


    Customer c[50];
    Employee e[50];

    
}
