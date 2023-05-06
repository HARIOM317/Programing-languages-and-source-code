#include<stdio.h>
#include<string.h>
typedef struct account{
    int accountNo;
    float amount;
    int year;
    char IFSC[20];
    char name[25];
}bank;
void display(bank c){
    for(int i=0; i<5; i++){
    printf("\nThe account number of customer %d is %d\n", i+1, c.accountNo);
    printf("The IFSC code of customer %d is %s\n", i+1, c.IFSC);
    printf("The Name of customer %d is %s\n", i+1, c.name);
    printf("The opening year of customer %d is %d\n", i+1, c.year);
    printf("The Amount of customer %d is %.2f\n", i+1, c.amount);
    printf("\n*****************************************************\n\n");
    }
}
int main(){
    bank customer[5];
    for(int i=0; i<5; i++){
        printf("\nEnter the account no. of customer %d \n", i+1);
        scanf("%d", &customer[i].accountNo);
        printf("Enter the amount of customer %d \n", i+1);
        scanf("%f", &customer[i].amount);
        printf("Enter opening year of customer %d \n", i+1);
        scanf("%d", &customer[i].year);
        printf("Enter the IFSC code of customer %d \n", i+1);
        scanf("%s", customer[i].IFSC);
        printf("Enter the Name of customer %d \n", i+1);
        scanf("%s", customer[i].name);
    }
    for(int i=0; i<5; i++){
        display(customer[i]);
    }
    return 0;
}