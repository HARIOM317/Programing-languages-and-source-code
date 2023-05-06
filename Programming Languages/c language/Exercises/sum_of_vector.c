#include<stdio.h>
struct vector{
    int x;
    int y;
};
struct vector sumvector(struct vector v1, struct vector v2){
    struct vector result;
    result.x = v1.x+v2.x;
    result.y = v1.y+v2.y;
    return result;
}
int main(){
  struct vector v1, v2, sum;
  v1.x = 5;
  v1.y = 7;
  
  v2.x = 5;
  v2.y = 10;

  sum = sumvector(v1, v2);
  printf("Sum of X dimension is: %d and Sum of Y dimension is: %d \n", sum.x, sum.y);
  
    return 0;
}