#include<stdio.h>
void print_table(int *mul_table, int num, int n){
    printf("The multiplication table of %d is \n\n", num);
    for(int i=0; i<n; i++){
        mul_table[i] = num*(i+1);
    }
    for(int i=0; i<n; i++){
        printf("%d x %d = %d \n", num, i+1, mul_table[i] );
    }
    printf("\n**********************************************************\n\n");
}
int main(){
    int mul_table[3][10];
    print_table(mul_table[0], 2, 10);
    print_table(mul_table[1], 7, 10);
    print_table(mul_table[2], 9, 10);

    return 0;
}