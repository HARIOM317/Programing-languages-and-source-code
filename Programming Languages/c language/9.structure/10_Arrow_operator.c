#include<stdio.h>
#include<string.h>

struct student{
    int math;
    int science;
    int computer;
    float result;
    char name[25];
};
int main(){
  struct student a1, a2;
  struct student *ptr;
  ptr = &a1;
  struct student *ptr1;
  ptr1 = &a2;

  (*ptr).math = 98;
  (*ptr).science = 97;
  (*ptr).computer = 98;
  float pers = (float)(a1.math+a1.science+a1.computer)/3;
  (*ptr).result = pers;
  strcpy((*ptr).name, "hariom"); 

  printf("\nThe marks of student a1 in math is: %d \n", a1.math); 
  printf("The marks of student a1 in science is: %d \n", a1.science); 
  printf("The marks of student a1 in computer is: %d \n", a1.computer); 
  printf("The result of student a1 is: %.2f \n", a1.result); 
  printf("The name of student a1 is: %s \n\n", a1.name); 

  printf("******************************************************\n\n");

  ptr1->math = 95;
  ptr1->science = 85;
  ptr1->computer = 95;
  float pers1 = (float)(a2.math+a2.science+a2.computer)/3;
  ptr1->result = pers1;
  strcpy(ptr1->name, "Abhishek"); 

  printf("The marks of student a2 in math is: %d \n", a2.math); 
  printf("The marks of student a2 in science is: %d \n", a2.science); 
  printf("The marks of student a2 in computer is: %d \n", a2.computer); 
  printf("The result of student a2 is: %.2f \n", a2.result); 
  printf("The name of student a2 is: %s \n\n", a2.name); 

    return 0;
}