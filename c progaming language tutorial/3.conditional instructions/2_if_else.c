 #include<stdio.h>
 
 int main(){
     int age;
     printf("Enter your age\n");
     scanf("%d", &age);
     if(age>=80){
         printf("you can not drive\n");
     }
     else{
         printf("you can drive and you can also go outside\n");
     }
     return 0;
 }