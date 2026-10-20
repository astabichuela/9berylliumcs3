class Publication: # creates the  class Publication
    def __init__(self, title, author): # defines and initializes the attributes
        self.__title = title # assigns value of the title 
        self.__author = author # assigns value of the author

    def get_title(self): # defines the method
        return self.__title # returns its value

    def get_author(self): # defines the method
        return self.__author # returns its value

    def set_title(self, title): # defines the method
        self.__title = title # sets value of the title

    def set_author(self, author): # defines the method
        self.__author = author # sets value of the author

    def display_info(self): # defines the method
        print(f"Title: {self.__title}") # prints the title
        print(f"Author: {self.__author}") # prints the author

class Book(Publication): # creates the class Book that inherits from Publication
    def __init__(self, title, author, number_of_pages): # defines and initializes the attributes
        super().__init__(title, author) # calls the attributes of the parent class Publication
        self.__number_of_pages = number_of_pages # assigns value of the number of pages

    def get_number_of_pages(self): # defines the method
        return self.__number_of_pages # returns its value

    def set_number_of_pages(self, number_of_pages): # defines the method
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("Number of pages must be positive.") # the whole 4 lines is the condition that checks for negative number of pages. if condition is not met, it prints something that tells it's wrong, if it's met, the value of the number of pages is set to the updated value.

class Magazine(Publication): # creates the class Magazine that inherits from Publication
    def __init__(self, title, author, issue_number): # defines and initializes the attributes
        super().__init__(title, author) # calls the attributes of the parent class Publication
        self.__issue_number = issue_number # assigns value of the issue number

    def get_issue_number(self): # defines the method
        return self.__issue_number # returns its value

    def set_issue_number(self, issue_number):  # defines the method
        self.__issue_number = issue_number # sets value of the issue number

# the objects are:
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("Natural Geographic", "Various Authors", 202)

# prints the information of publication, book, and magazine 
print("\nPublication Information: ")
pub1.display_info()

print("\nBook Information: ")
book1.set_number_of_pages(-310) # tries to set an invalid number
book1.display_info()
print(f"Number of Pages: {book1.get_number_of_pages()}")

print("\nMagazine Information: ")
mag1.display_info()
print(f"Issue number: {mag1.get_issue_number()}")
