#include<stdio.h>
#include<string.h>

struct employee{
    int code;
    float salary;
    char name[20];
};
int main(){
  struct employee facebook[100];
  
  facebook[0].code = 101;  
  facebook[0].salary = 10000;  
  strcpy(facebook[0].name, "hariom");  

  facebook[1].code = 102;  
  facebook[1].salary = 100000.25;  
  strcpy(facebook[1].name, "abhishek");  

  facebook[2].code = 103;  
  facebook[2].salary = 50000;  
  strcpy(facebook[2].name, "rahul");  

  facebook[3].code = 104;  
  facebook[3].salary = 70000;  
  strcpy(facebook[3].name, "geeta");  

  facebook[4].code = 105;  
  facebook[4].salary = 1000000;  
  strcpy(facebook[4].name, "raju");  


  printf("The 1st employee code is: %d\n", facebook[0].code);
  printf("The 1st employee salary is: %.2f\n", facebook[0].salary);
  printf("The 1st employee name is: %s\n\n", facebook[0].name);

  printf("The 2nd employee code is: %d\n", facebook[1].code);
  printf("The 2nd employee salary is: %.2f\n", facebook[1].salary);
  printf("The 2nd employee name is: %s\n\n", facebook[1].name);

  printf("The 3rd employee code is: %d\n", facebook[2].code);
  printf("The 3rd employee salary is: %.2f\n", facebook[2].salary);
  printf("The 3rd employee name is: %s\n\n", facebook[2].name);

  printf("The 4th employee code is: %d\n", facebook[3].code);
  printf("The 4th employee salary is: %.2f\n", facebook[3].salary);
  printf("The 4th employee name is: %s\n\n", facebook[3].name);

  printf("The 5th employee code is: %d\n", facebook[4].code);
  printf("The 5th employee salary is: %.2f\n", facebook[4].salary);
  printf("The 5th employee name is: %s\n\n", facebook[4].name);

    return 0;
}