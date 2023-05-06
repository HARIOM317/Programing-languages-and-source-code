#include<stdio.h>

int main(){
    FILE *ptr;
    char employee1[20];
    char employee2[20];
    float salary1;
    float salary2;

    printf("enter the name of 1st employee \n");
    gets(employee1);
    
    printf("enter the salary of 1st employee \n");
    scanf("%f", &salary1);

    printf("enter the name of 2st employee \n");
    scanf("%s", employee2);
    
    printf("enter the salary of 2st employee \n");
    scanf("%f", &salary2);

    ptr = fopen("employee_salary.txt", "w");
    fprintf(ptr, "%s, %.2f\n", employee1, salary1);
    fprintf(ptr, "%s, %.2f\n", employee2, salary2);
    
    fclose(ptr);
    printf("your data successfully made in employee_salary.txt");
    return 0;
}