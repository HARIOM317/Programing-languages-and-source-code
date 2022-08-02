#include<stdio.h>

    void GoodMorning();
    void GoodAfternoon();
    void GoodNight();
int main(){
    GoodMorning();
    return 0;
}
void GoodMorning(){
    printf("good morning HSR \n");
     GoodAfternoon();
}
void GoodAfternoon(){
    printf("good afternoon HSR \n");
    GoodNight();
}
void GoodNight(){
    printf("good Night HSR \n");
}  