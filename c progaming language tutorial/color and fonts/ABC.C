#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>

int main(){
   char *emojis[5] = {u8"😀", u8"🥰", u8"😓", u8"🥱", u8"😂"};
   srand(time(NULL));
   int randomint = rand() % 5;
   printf("Your mood is %s", emojis[randomint]);
    return 0;
}