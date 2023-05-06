#include <iostream>

using namespace std;

/*
Given a "2 x n" board and tiles of size "2 x 1", count the number of ways to tile the given board using these tiles.
*/

int tilingWays(int n){
    if (n==0){
        return 0;
    }
    if (n==1){
        return 1;
    }
    // it is just like fibonacci sequence.
    return tilingWays(n-1) + tilingWays(n-2);
}

int main(){
    cout<<tilingWays(4)<<endl;

    return 0;
}