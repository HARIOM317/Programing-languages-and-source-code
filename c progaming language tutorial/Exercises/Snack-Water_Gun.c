#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<time.h>

int SnakeWaterGun(char you, char computer){
    // Match draw condision.
    if(you == computer){
        return 0;
    }

    // Match Nondraw condision.
    if(you=='s' && computer=='w'){
        return 1;
    }
    else if(you=='w' && computer=='s'){
        return -1;
    }

    if(you=='w' && computer=='g'){
        return 1;
    }
    else if(you=='g' && computer=='w'){
        return -1;
    }

    if(you=='g' && computer=='s'){
        return 1;
    }
    else if(you=='s' && computer=='g'){
        return -1;
    }


}

int main(){
    char you, computer;
    srand(time(0));
    int number = rand()%100+1;

    if(number<33){
        computer = 's';
    }
    else if(number>33 && number<66){
        computer = 'w';
    }
    else{
        computer = 'g';
    }

    printf("\n*****ENTER 'S' FOR SNAKE, 'W' FOR WATER AND 'G' FOR GUN*****\n");
    scanf("%c", &you);

    int result = SnakeWaterGun(you, computer);

    if(result == 0){
        printf("*** 'MATCH DRAW' ***\n");
    }
    else if(result == 1){
        printf("*** 'YOU WON!' ***\n");
    }
    else{
        printf("*** 'YOU LOSE!' ***\n");
    }
    printf("\n YOU CHOOSE '%c' AND COMPUTER CHOOSE '%c' \n\n", you, computer);
    printf("\n*******************************************************\n\n");

    getch();
    return 0;
}