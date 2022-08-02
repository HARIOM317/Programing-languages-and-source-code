#include<stdio.h>
#include<time.h>

int main(){
    time_t myTime = time(NULL);
    printf("%s", ctime(&myTime));
    return 0;
}