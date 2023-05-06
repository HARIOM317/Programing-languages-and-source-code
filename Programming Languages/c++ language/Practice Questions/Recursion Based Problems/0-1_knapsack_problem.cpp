#include <iostream>

using namespace std;

/*
put n items with given weight and value in a knapsack of capacity W to get the maximum total value in the knapsack.
1. weight should be less then capacity of knapsack.
2. value or price of item should be maximum.

ex - 
items        -      0   1   2
weight[item] -      10  20  30
value[item]  -      100 50  150

and W (capacity of knapsack) = 50

ans = 250 (100+150 and weight is also less then W)
*/

int knapsack(int value[], int wt[], int n, int W){

    if (n==0 || W==0){
        return 0;
    }

    if (wt[n-1] > W){
        return knapsack(value, wt, n - 1, W);
    }

    // first recursion for if we include the item and second recursion for if we skip the item.
    return max(knapsack(value, wt, n-1, W-wt[n-1]) + value[n-1], knapsack(value, wt, n-1, W));
}

int main(){
    int wt[] = {10, 20, 30};
    int value[] = {100, 50, 150};
    int W = 50, n=3;

    cout<<knapsack(value, wt, n, W)<<endl;
    return 0;
}