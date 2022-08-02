#include<stdio.h>

int main(){
    int Roll_No;
    printf("Enter your roll number\n");
    scanf("%d", &Roll_No);
    if(Roll_No == 1001){
        printf("your Roll Number is 1001 and you are accepted for selection\n");
    }
    else if (Roll_No == 1002){
        printf("your Roll Number is 1002 and you are accepted for selection\n");
    }   
     else if (Roll_No == 1003){
        printf("your Roll Number is 1003 and you are accepted for selection\n");
    }  
     else if (Roll_No == 1004){
        printf("your Roll Number is 1004 and you are accepted for selection\n");
    }  
     else if (Roll_No == 1005){
        printf("your Roll Number is 1005 and you are accepted for selection\n");
    }   
    else{
        printf("your roll is not resisterede with us! (you can not participate)\n");
    }
    return 0;
}