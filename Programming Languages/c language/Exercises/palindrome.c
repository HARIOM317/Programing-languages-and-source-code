#include<stdio.h>
int palindrome(int num){\
int reversed = 0;
int originalNumber = num;
while(num != 0){
    reversed = reversed*10 + num%10;
    num = num/10;
}
printf("The reverse number is:  %d \n", reversed);
if(originalNumber == reversed){
    return 1;
}
else{
    return 0;
}

}
int main(){
    int number;
    printf("\n\nEnter a number to check whether a number is polindrom or not: \n");
    scanf("%d", &number);

    if(palindrome(number)){
        printf("This is a palindrom number \n\n\n");
    }
    else{
        printf("This is not a palindrom number \n\n\n");
    }
    return 0;
}