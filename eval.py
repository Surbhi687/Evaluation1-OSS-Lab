
library={}

def add_book(bname, bauthor, bISBN, bgenre, bstatus):
    library[bISBN] = {
    "name" : bname,
    "author" : bauthor,
    "genre" : bgenre,
    "status" : bstatus
    }

def update_book_details(newname, newauthor, bISBN, newgenre, newstatus):
    if bISBN in library:
        library[bISBN]["name"] = newname
        library[bISBN]["author"] = newauthor
        library[bISBN]["genre"] = newgenre
        library[bISBN]["status"] = newstatus
    else:
        return

def search_by_isbn(bISBN):
    if bISBN in library:
        print(library[bISBN])
    else:
        print("this ISBN is not availbale\n")



add_book("harry potter", "jk rowling", "001", "fantasy", "available")
add_book("murder in paris", "agatha cristie", "002", "mystery", "available")
add_book("pride and prejudice", "jane austen", "003", "historical", "not available")

print(library)

print(f"Search result:")
search_by_isbn("002")
print("\n")

update_book_details("potterhead", "jk rowling", "001", "mystery", "not available")

print(library)

