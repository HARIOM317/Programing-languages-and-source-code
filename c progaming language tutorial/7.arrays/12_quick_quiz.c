#include<stdio.h>
void display(int ptr[3][5]){
    for(int i=0; i<3; i++){
        for(int j=0; j<5; j++){
            printf("Enter the marks of student %d in subject %d \n", i+1, j+1);
            scanf("%d", &ptr[i][j]);
        }
    }
    for(int i=0; i<3; i++){
        for(int j=0; j<5; j++){
            printf("The marks of student %d in subject %d is %d \n", i+1, j+1, ptr[i][j]);
        }
    }
}
int main(){
    int marks[3][5];
    display(marks);
    getch();
    return 0;
}