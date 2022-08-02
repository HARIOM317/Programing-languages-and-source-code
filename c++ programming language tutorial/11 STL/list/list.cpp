#include<iostream>
#include<list>

using namespace std;

void display(list<int>&lst){
    list<int>::iterator it;
    for(it=lst.begin(); it!=lst.end(); it++){
        cout<<*it<<"  ";
    }cout<<endl;
}

int main()
{
    list<int>list1;
    list1.push_back(5);
    list1.push_back(8);
    list1.push_back(45);
    list1.push_back(7);
    list1.push_back(9);
    list1.push_back(9);
    list1.push_back(12);

    cout<<"Elements of list1 : ";
    display(list1);

    //reversing the list1
    cout<<"After reversing the elements are : ";
    list1.reverse();
    display(list1);

    //Sorting the list
    cout<<"After sorting the elements are : ";
    list1.sort();
    display(list1);

    cout<<"After deletion the elements are : ";
    list1.pop_back();//it will remove last element
    list1.pop_front();//it will remove first element
    list1.remove(9);//it will remove element from center which element we will pass 

    display(list1);


    // list<int>::iterator iter;
    // iter = list1.begin();

    // cout<<*iter<<"  ";
    // iter++;
    // cout<<*iter<<"  ";
    // iter++;
    // cout<<*iter<<"  ";
    // iter++;
    // cout<<*iter<<"  ";
    // iter++;
    // cout<<*iter<<"  ";
    // iter++;
    // cout<<*iter<<"  ";
    // iter++;
    // cout<<*iter<<"  ";
    // iter++;

    list<int>list2(4);
    list<int>::iterator itr;
    itr = list2.begin();
    *itr = 78;
    itr++;
    *itr = 48;
    itr++;
    *itr = 21;
    itr++;
    *itr = 98;
    itr++;
    cout<<"Elements of list2 are ; ";
    display(list2);

    list1.sort();  //sort list 1
    list2.sort();  //sort list 2
    //Merge both lists
    list1.merge(list2);
    cout<<"List 1 after merging :  ";
    display(list1);

    return 0;
}