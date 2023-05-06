 #include<stdio.h>
 
 int main(){
     int age;
     printf("Enter your age\n");
     scanf("%d", &age);
     if(age>=18 && age<=80){
         printf("you can drive and you can also go outside by using your wheecal\n");
     }
     else{
         printf("you can not drive\n");
     }
     return 0;
 }