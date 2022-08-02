#include<stdio.h>

int main(){
    FILE *ptr;
    int num;
    printf("enter the number for making a table \n");
    scanf("%d", &num);
    ptr = fopen("multiplication_table.txt", "w");
    for(int i=0; i<10; i++){
        fprintf(ptr, "%d X %d = %d \n", num, i+1, num*(i+1));
    }
    fclose(ptr);
    printf("your table successfully made in multiplication_table.txt");
    return 0;
}