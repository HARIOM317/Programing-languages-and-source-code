#include <iostream>

using namespace std;

/*
problem - count the number of paths possible from start point to end point in game-board.

ex - 0 1 2 3
paths start from 0- first path = 0-1, 1-2, 2-3
                    second path = 0-2, 2-3
                    second path = 0-1, 1-3
                    second path = 0-3
 ans - 4

paths start from 1- first path = 1-2, 2-3
                    second path = 1-3
 ans - 2

paths start from 2- first path = 2-3
 ans - 1

paths start from 3- first path = 3-3
 ans - 1
*/

int countPath(int s, int e){
    if(s==e){
        return 1;
    }
    if(s>e){
        return 0;
    }
    // for dice
    int count = 0;
    for (int i = 1; i <= 6; i++)
    {
        count += countPath(s+i, e);
    }
    return count;
}

int main(){
    cout<<"All possible paths from 0-3 = "<< countPath(0, 3)<<endl;
    cout<<"All possible paths from 1-3 = "<< countPath(1, 3)<<endl;
    cout<<"All possible paths from 2-3 = "<< countPath(2, 3)<<endl;
    cout<<"All possible paths from 3-3 = "<< countPath(3, 3)<<endl;

    return 0;
}