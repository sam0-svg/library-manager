
class Library:
        
        def __init__(self):
            self.books_list = []

        def add_book(self, title, author):
            self.books_list.append({"Title":title, "Author":author})
            return f"This book has been added to your library,{title} from {author}"

        def remove_book(self, title):
            
            for book in self.books_list:
                if book['Title'] == title:
                    self.books_list.remove(book)
                    return f"This has been removed from your library: {book['Title']}"
                    
            return "Your book has not been found"

            

        def search_book(self, title):
            
            for book in self.books_list:
                if book['Title'] == title:
                    return f"Your book {title} is available"
            return "Book has not been found."
                
            

        def show_books(self):
            book = []
            for books in self.books_list:
                book.append(f"{books['Title']}: {books['Author']}")
                
            return "\n".join(book)

        




