#include<stdio.h>

int main(){
    int radius;
    int hight;
    float pi = 3.14;

    printf("what is the radius\n");
    scanf("%d", &radius);

    printf("the area of this circle is %f \n",pi*radius*radius);

    printf("What is the hight of the cylinder\n");
    scanf("%d", &hight);

    printf("the volume of this cylinder is %f",pi*radius*radius*hight);
    return 0;
}