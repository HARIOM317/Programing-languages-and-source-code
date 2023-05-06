#include <bits/stdc++.h>

using namespace std;

class Library{
    public:
    string books[100];
    int noOfBooks = 0;
    Library(){
        string defaultBooks[] = {"KGF", "RRR", "I am back", "Advanced Java", "Python", "You & Me", "Let's code", "OOPs", "King", "The Jungle Books"};
        for(int i = 0; i < 10; i++){
            books[i] = defaultBooks[i];
            noOfBooks++;
        }
    }
};

class Book : public Library{
    public:
    void addBook(string bookName){
        this->books[noOfBooks] = bookName;
        noOfBooks++;
        cout<<"The book "<<bookName<<" added successfully!"<<endl;
    }

    void showBooks(){
        if(noOfBooks == 0){
            cout<<"\nSorry, No any book available!\n"<<endl;
        }
        else{
            cout<<"\n\n_____ Available Books _____\n\n";
            int n = 1;
            for (int i = 0; i < noOfBooks; i++)
            {
                if(books[i] == ""){
                    continue;
                }
                cout<<n<<". "<<books[i]<<endl;
                n++;
            }
            cout<<endl;
        }
    }

    void issueBook(string bookName, string studentName){
        for (int i = 0; i < noOfBooks; i++)
        {
            if (this->books[i] == "")
            {
                continue;
            }
            if(this->books[i] == bookName){
                cout<<"The book "<<bookName<<" has been issued to "<<studentName<<" successfully!"<<endl;
                this->books[i] = "";
                return;
            }
        }
        cout << "Sorry, book " << bookName << " is currently not available!" << endl;
    }

    void returnBook(string bookName, string studentName){
        this->books[noOfBooks] = bookName;
        noOfBooks++;
        cout<<"The book "+bookName<<" has been returned by "<<studentName<<endl;
    }
};


int main(){
    Book b1;
    b1.showBooks();
    b1.addBook("The power of Bhagvat Geeta");
    b1.addBook("Ruby");
    b1.addBook("basic c language");
    b1.addBook("The big bank theory");
    b1.addBook("The kashmir files");
    b1.showBooks();

    b1.issueBook("Python", "Abhishek");
    b1.issueBook("Ruby", "Hariom");
    b1.showBooks();

    b1.returnBook("Ruby", "Hariom");
    b1.showBooks();

    return 0;
}