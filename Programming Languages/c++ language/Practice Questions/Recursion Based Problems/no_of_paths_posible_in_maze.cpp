#include <iostream>

using namespace std;

/*
problem - count the number of paths possible in a maze and we can only move either left-right or top-bottom direction.
*/

int countPathMaze(int n, int i, int j){
    // condition for ending point
    if(i==n-1 && j==n-1){
        return 1;
    }

    // condition when path is not possible
    if(i>=n || j>=n){
        return 0;
    }

    return countPathMaze(n, i+1, j) + countPathMaze(n, i, j+1);
}

int main(){
    cout<<countPathMaze(3, 0, 0)<<endl;    

    return 0;
}