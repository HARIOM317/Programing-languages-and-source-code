#include<stdio.h>
#include<conio.h>

int main(){
    int h, s, m, i;

    printf("\e[?25l");
    printf("\nEnter the time in formate of HH:MM:SS \n\n");
    printf("Enter hours\n");
    scanf("%d", &h);
    printf("Enter minutes\n");
    scanf("%d", &m);
    printf("Enter seconds\n");
    scanf("%d", &s);

    while(h<24){
        while(m<60){
            while(s<60){
                sleep(1);
                system("CLS");
                printf("\n \033[95;3;1m **********************************");
                printf("\033[92;3;1m ===================================");
                printf("\033[94;3;1m **********************************");

                printf("\n \033[95;3;1m **********************************");
                printf("\033[92;3;1m ===================================");
                printf("\033[94;3;1m **********************************\n\n");


                
                printf("\033[33;3;1m \t\t\t\t\t\t HH : MM : SS \n"); 
                s++;

                printf("\033[36;3;1m \t\t\t\t\t\t %d : %d : %d \n", h, m, s);

                printf("\n \033[95;3;1m **********************************");
                printf("\033[92;3;1m ===================================");
                printf("\033[94;3;1m **********************************");

                printf("\n \033[95;3;1m **********************************");
                printf("\033[92;3;1m ===================================");
                printf("\033[94;3;1m **********************************\n\n");

            }
            m++;
            s=0;
        }
    h++;
    m=0;    
    }
    getch();
    return 0;

}