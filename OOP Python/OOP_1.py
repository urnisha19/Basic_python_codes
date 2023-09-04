# creating a class named StoryBook
class StoryBook:
    pass


# print(StoryBook)  # output:class '__main__.StoryBook'

# creating an instance/object of the StoryBook class
book_1 = StoryBook()  # here  StoryBook() means an instance/class of  StoryBook class
# print(book_1)  # output: __main__.StoryBook object at 0x000002997440BFD0

# creating instance variable
# instance variable holo 1ta instance er kisu property
# object er nam er pot dot diye object e attribute/variable add kora hoy
book_1.name = "Hamlet"
book_1.price = 350
book_1.author = "Shakespeare"
book_1.author_born = 1564

# creating another instance of storybook class
book_2 = StoryBook()
book_2.name = "The Kite Runner"
book_2.price = 280
book_2.author = "Khaled Hossaini"
book_2.author_born = 1965

print(book_1.name)
print(book_2.name)
