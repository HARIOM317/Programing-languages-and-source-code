#include<stdio.h>
#include<string.h>
struct employee{
    int code;
    float salary;
    char name[20];
};
int main(){
  struct employee hariom = {101, 50000.25, "Hariom"};
  struct employee a1 = {102, 70000.25, "pooja"};
  struct employee a2 = {103, 20000.25, "abhishek"};


  printf("code is: %d \n", hariom.code);
  printf("salary is: %f \n", hariom.salary);  
  printf("name is: %s \n\n", hariom.name);  

  printf("code is: %d \n", a1.code);
  printf("salary is: %f \n", a1.salary);  
  printf("name is: %s \n\n", a1.name);  

  printf("code is: %d \n", a2.code);
  printf("salary is: %f \n", a2.salary);  
  printf("name is: %s \n\n", a2.name);  

    return 0;
}