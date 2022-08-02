#include<stdio.h>
typedef struct date{
    int date;
    int month;
    int year;
    int hour;
    int minite;
    int second;
}date;
void display(date d){
    printf("The date & time is: %d/%d/%d %d:%d:%d \n", d.date, d.month, d.year, d.hour, d.minite, d.second);
}
int datecmp(date d1, date d2){
    if(d1.year>d2.year){
        return 1;
    }
    if(d1.year<d2.year){
        return -1;
    }
    if(d1.month>d2.month){
        return 1;
    }
    if(d1.month<d2.month){
        return -1;
    }
    if(d1.date>d2.date){
        return 1;
    }
    if(d1.date<d2.date){
        return -1;
    }
    if(d1.hour>d2.hour){
        return 1;
    }
    if(d1.hour<d2.hour){
        return -1;
    }
    if(d1.minite>d2.minite){
        return 1;
    }
    if(d1.minite<d2.minite){
        return -1;
    }
    if(d1.second>d2.second){
        return 1;
    }
    if(d1.second<d2.second){
        return -1;
    }
        return 0;
}
int main(){
    date d1 = {30, 11, 2021, 12, 45, 59};
    date d2 = {22, 9, 2022, 7, 36 ,50};

    display(d1);
    display(d2);

    int a = datecmp(d1,d2);
    printf("Date & time comparision function returns: %d \n", a);
    
    return 0;
}