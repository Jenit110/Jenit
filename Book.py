class library:
    def __init__(self,books):
        self.books = books
   
    def list_books(self):
        print("Available Books...!!")
        for book in self.books:
            print(book)

    
    
    


books=['python','jave','c++','javescript','Ruby']
o = library(books)

msg = """
1. Display Books
2. Add Book
3. Borrow Book
4. Return Book
5. Delete Book
6. Exit
"""

while True:
   print(msg)
   choice = int (input("Enter your choice:"))
   if choice == 1:
       o.list_books()

   1

