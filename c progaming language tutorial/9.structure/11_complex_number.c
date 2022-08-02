#include<stdio.h>
struct complax{
    int x;
    int y;
};
int main(){
  struct complax c1, c2, c3;

  printf("Enter a and b where a+ib is the first complax number \n");
  scanf("%d%d", &c1.x, &c1.y);
    printf("Enter c and d where c+id is the second complax number \n");
  scanf("%d%d", &c2.x, &c2.y);
  c3.x = c1.x+c2.x;
  c3.y = c1.y+c2.y;

printf("Sum of the complax numbers is: (%d+%di)\n", c3.x, c3.y);
    return 0;
}