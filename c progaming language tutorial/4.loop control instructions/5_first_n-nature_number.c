#include<stdio.h>

int main(){
    int n;
    printf("Enter the value of n\n");
    scanf("%d", &n);
    for(int i=1; i<=n; i++){
        printf("%d\n", i);
    }
    return 0;
}