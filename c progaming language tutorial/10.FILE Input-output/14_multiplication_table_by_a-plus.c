#include<stdio.h>

int main(){
    FILE *ptr;
    int num;
    ptr = fopen("multiplication_table2.txt", "a+");
if(!ptr){
    printf("Can't created a file \n");
}
else{
    printf("enter the number for making a table \n");
    scanf("%d", &num);

    fprintf(ptr, "\n=======*****%d*****=======\n\n", num);

    for(int i=0; i<10; i++){
        fprintf(ptr, "%d X %d = %d \n", num, i+1, num*(i+1));
    }
    fclose(ptr);
    printf("your table successfully made in multiplication_table2.txt");
}
    
    return 0;
}