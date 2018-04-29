"""
This program checks for curse words in a piece of text and alerts the user
"""

def read_text():
    quotes = open(r"C:\Users\gopir\Documents\Gopi\Education\Github\Udacity\Programming_Foundations_with_Python\Profanity Editor\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

read_text()