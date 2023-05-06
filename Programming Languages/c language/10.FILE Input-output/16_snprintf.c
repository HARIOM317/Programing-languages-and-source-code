#include<stdio.h>
#include<string.h>

int main(){
    int num;
    FILE *ptr;
    char pattern[20];
    char multiplication_table2[30];
    int isMatched = 0;
    int tableCount = 1;
    ptr = fopen("multiplication_table2.txt", "r");
    if(!ptr){
        printf("can't creat file");
    }
    else{
        printf("please enter a number for taking the table from text file \n");
        scanf("%d", &num);

        snprintf(pattern, 20, "=======*****%d*****=======\n", num);

        while(fgets(multiplication_table2, 30, ptr)!= NULL){
            if(isMatched && tableCount <= 10){
                printf("%s", multiplication_table2);
                tableCount++;
            }
            if(!strcmp(multiplication_table2, pattern)){
                isMatched = 1;
            }
        }
        fclose(ptr);
    }
    return 0;
}