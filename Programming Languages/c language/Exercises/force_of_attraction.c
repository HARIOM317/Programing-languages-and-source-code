#include<stdio.h>
float force(float mass);
int main(){
    int a;
    printf("Enter the value of mass \n");
    scanf("%d", &a);
    printf("The value of force in newton is %.2f \n", force(a));
    return 0;
}
float force(float mass){
    float result = mass*9.8;
    return result;

}