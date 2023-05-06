#include<stdio.h>
typedef struct time{
    int hour;
    int minite;
    int second;
}time;
void display(time t){
    printf("The time is: %d:%d:%d \n",t.hour, t.minite, t.second);
}
int timecmp(time t1, time t2){
    if(t1.hour>t2.hour){
        return 1;
    }
     if(t1.hour<t2.hour){
        return -1;
    }
    if(t1.minite>t2.minite){
        return 1;
    }
     if(t1.minite<t2.minite){
        return -1;
    }
    if(t1.second>t2.second){
        return 1;
    }
     if(t1.second<t2.second){
        return -1;
    }
    return 0;
}
int main(){
    time t1 = {5, 45, 48};
    time t2 = {12, 25, 55};
    display(t1);
    display(t2);

    int a = timecmp(t1, t2);
    printf("The time comparision result is: %d \n", a);
    return 0;
}