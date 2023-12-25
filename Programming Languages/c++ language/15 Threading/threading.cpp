#include <iostream>
#include <thread>

using namespace std;

void taskA(){
    for (int i = 0; i < 10; i++)
    {
        printf("Task A: %d\n", i);
        fflush(stdout);
    } 
}

void taskB(int n){
    for (int i = 0; i < n; i++)
    { 
        printf("\nTask B: %d\n", i);
        fflush(stdout);
    }
    
}

int main(){
    thread t1(taskA);
    thread t2(taskB, 10);

    t1.join();
    t2.join();

    return 0;
}