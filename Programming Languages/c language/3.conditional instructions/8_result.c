#include<stdio.h>

int main(){
    int physics,chemistry,maths;
    float total;

    printf("enter physics marks\n");
    scanf("%d", &physics);

    printf("enter chemistry marks\n");
    scanf("%d", &chemistry);

    printf("enter maths marks\n");
    scanf("%d", &maths);

    total = (physics+chemistry+maths)/3;
    if((total<40) || physics<33 || chemistry<33 || maths<33){
        printf("your total percentage is %f and you are fail\n",total);
    }

    else{
        printf("your total percentage is %f and you are pass\n",total);
    }
    return 0;
}