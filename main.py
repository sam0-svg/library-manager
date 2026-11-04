from mylibrary.library import Library

   
def main():
    while True:
        answer = input("Enter your command(e:Exit, a:Add books, r:Remove books, s:Search books, sh:Show books): ")
    
        if answer == "e":
            print("Exiting program")
            break

        elif answer == "a":

            book_name = input("Please enter your book's name: ").strip()
            book_author = input("Please enter your author's name: ").strip()
            if not book_name or not book_author :
                print("You can't add spaces")
            else:
                print(lib.add_book(book_name, book_author))
            

        
        

        elif answer == "r":
            book_name = input("Please enter your book's name: ")
            print(lib.remove_book(book_name))
         

        elif answer == "s":
            book_name = input("Please enter your book's name: ")
            print(lib.search_book(book_name))
         

        elif answer == "sh":
            if not lib.show_books():
                print("Library is empty.")
            else:
                print(lib.show_books())

        else:
            print("Invalid input.")

         
if __name__ == "__main__":
    lib = Library()
    print("Hi welcome to library program, here you can manage your books.")
    main()
