#include<stdio.h>
void decrypt(char *c){
    char *ptr = c;
    while(*ptr!='\0'){
        *ptr = *ptr-1;
        ptr++;
    }
}
int main(){
    char c[] = "Hppe!Npsojoh";
    decrypt(c);
    printf("Decrypt string is: %s \n", c);
    return 0;
}