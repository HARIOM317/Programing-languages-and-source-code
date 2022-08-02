#include<stdio.h>

int main(){
    int n_student = 3;
    int n_subject = 5;
    int marks[3][5];
    for(int i=0; i<n_student; i++){
        for(int j=0; j<n_subject; j++){
                printf("Enter the marks of student %d in subject %d \n", i+1, j+1);
                scanf("%d", &marks[i][j]);
            } 
        }

    for(int i=0; i<n_student; i++){
        for(int j=0; j<n_subject; j++){
                printf("The marks of student %d in subject %d is %d \n", i+1, j+1, marks[i][j]);
            }
        }
    return 0;
}