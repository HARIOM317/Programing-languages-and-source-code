#include <stdio.h>
#include <string.h>

void salting_in_pass(char pass[])
{
    char salt[] = "#@123%321$DONE";
    char new_password[200];
    strcpy(new_password, pass);
    strcat(new_password, salt);
    printf("New password is : %s", new_password);
}

int main()
{
    char password[100];
    printf("Enter password : ");
    scanf("%s", password);

    salting_in_pass(password);

    return 0;
}