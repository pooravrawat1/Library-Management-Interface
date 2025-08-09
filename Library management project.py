import Return
import ListSplit
import DateandTime
import Borrow

def start():
    while(True):
        print("                                     ")
        print("                                     ")
        print("       Library Management System     ")
        print("    By-Poorav Rawat and Pari Gupta   ")
        print("--------------------------------------------")
        print("Enter 1. To Display all books")
        print("Enter 2. To Issue a book")
        print("Enter 3. To Return a book")
        print("Enter 4. To Exit")
        try:
            a=int(input("Select a choice from 1-4: "))
            print()
            if(a==1):
                with open("stock.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
   
            elif(a==2):
                ListSplit.listSplit()
                Borrow.borrowBook()
            elif(a==3):
                ListSplit.listSplit()
                Return.returnBook()
            elif(a==4):
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            print("Please input as suggested.")
start()
