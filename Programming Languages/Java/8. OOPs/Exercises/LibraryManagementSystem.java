import java.util.Scanner;
class Library{
    public String[] books;
    public int noOfBooks;
    Scanner sc = new Scanner(System.in);

    Library(){
        this.books = new String[100];
        this.noOfBooks = 0;

        String[] defaultBooks = {"Think and grow", "The machine learning", "My java", "The python", "Advance C++", "Object Oriented Programming", "My life, My way", "Business analysis", "Social networking", "Health is Wealth", "Kotlin"};

        for (String element: defaultBooks){
            this.books[noOfBooks] = element;
            noOfBooks++;
        }
    }

    void addBook(){
        String book;
        System.out.print("\nEnter new book name : ");
        book = sc.nextLine();
        this.books[noOfBooks] = book;
        noOfBooks++;
        System.out.println("The book \""+book+"\" has been added successfully!");
    }

    void showAvailableBooks(){
        int n = 1;
        System.out.println("\n<<<<< The Available books are >>>>>\n");
        for (String book:this.books){
            if (book == null){
                continue;
            }
            System.out.println(n+". "+book);
            n++;
        }
    }

    void issueBook(){
        String bookName;
        System.out.print("\nEnter book name : ");
        bookName = sc.nextLine();

        for (int i = 0; i<this.books.length; i++){
            if (this.books[i]==null){
                continue;
            }
            if (this.books[i].equals(bookName)){
                System.out.println("The book \""+bookName+"\" has been issued!");
                this.books[i] = null;
                return;
            }
        }
        System.out.println("Sorry, this book \""+bookName+"\" is currently not available!");
    }

    void returnBook(){
        String book;
        System.out.print("\nEnter book name : ");
        book = sc.nextLine();
        this.books[noOfBooks] = book;
        System.out.println("The book \""+book+"\" has been returned!");
        noOfBooks++;
    }
}

public class LibraryManagementSystem {
    public static void main(String[] args) {
        Library theMiddleLibrary = new Library();
        Scanner sc = new Scanner(System.in);

        while (true){
            System.out.println("\nEnter 1 to Show all available books");
            System.out.println("Enter 2 to Issue a book");
            System.out.println("Enter 3 to Return a book");
            System.out.println("Enter 4 to Add a new book");
            System.out.println("Enter 5 to Exit");
            System.out.print("Choice : ");
            int choice = sc.nextInt();

            if (choice == 1){
                theMiddleLibrary.showAvailableBooks();
            }
            else if(choice == 2){
                theMiddleLibrary.issueBook();
            }
            else if(choice == 3){
                theMiddleLibrary.returnBook();
            }
            else if(choice == 4){
                theMiddleLibrary.addBook();
            }
            else if(choice == 5){
                System.out.println("Exiting...");
                break;
            }
            else {
                System.out.println("Invalid choice");
            }
        }
    }
}
