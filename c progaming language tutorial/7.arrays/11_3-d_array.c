#include<stdio.h>

int main(){
    int n_student = 3;
    int n_subject = 5;
    int n_school = 2;
    int marks[3][5][2];
    for(int i=0; i<n_student; i++){
        for(int j=0; j<n_subject; j++){
            for(int k =0; k<n_school; k++){
                printf("Enter the marks of student %d in subject %d of school %d\n", i+1, j+1, k+1);
                scanf("%d", &marks[i][j][k]);
            } 
        }
    }

    for(int i=0; i<n_student; i++){
        for(int j=0; j<n_subject; j++){
            for(int k =0; k<n_school; k++){
            printf("The marks of student %d in subject %d of school %d is %d \n", i+1, j+1, k+1, marks[i][j][k]);
            }
        }
    }
    return 0;
}