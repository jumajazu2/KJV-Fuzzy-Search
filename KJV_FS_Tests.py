import json

from fuzzysearch import find_near_matches 
#some faster libraries here: https://medium.com/codex/best-libraries-for-fuzzy-matching-in-python-cbb3e0ef87dd

# Load the JSON file
with open('C:/Users/Juraj/Documents/IT/Python/KJV_fuzzy_search/kjv.json', 'r') as file:
    data = json.load(file)
"""
print(type(data))

print(data["language"])

print(len(data["books"][1]["name"]))

print(range(len(data["books"][65]["chapters"][0]["verses"][1]["text"])))

books = len(data["books"]) #find the number of books
for book in range(books):
    print((data["books"][book]["name"]))

    chapters = len(data["books"][book]["name"]) #this should give the number of chapters in each book, but it gives the character count of the book name
    print(chapters)
print(books)
"""

def book_chapters(book_no):  #function to return chapter count for a specific book
    book_index = book_no - 1
    number_chapters = len(data["books"][book_index]["chapters"])
    return number_chapters

def chapter_verses(book_no, chapter_no): #function to return verse count for a specific chapter in a book
    book_index = book_no - 1
    chapter_index = chapter_no - 1
    number_verses = len(data["books"][book_index]["chapters"][chapter_index]["verses"])
    return number_verses


def get_verse (book_no, chapter_no, verse_no):  #return a specific verse
    book_index = book_no - 1
    chapter_index = chapter_no - 1
    verse_index = verse_no -1

    verse = (data["books"][book_index]["chapters"][chapter_index]["verses"][verse_index]["text"])

    return verse

def clean_list (query_string):
    query_string = query_string.upper() #make whole string uppercase
    mydict = {46: None, 44: None, 59: None, 63: None, 34: None, 45: None} # remove . , ; ? " -
    query_string = query_string.translate(mydict) #remove punctuation from whole string
    query_list = query_string.split()
    return query_list

def compare (query_string, base_string):
    query_string = clean_list(query_string) #turn query string into a list containing its uppercase words, stripped of any punctuation
    base_string = clean_list(base_string) #turn base KJV string into a list containing its uppercase words, stripped of any punctuation
    total_found = 0
    for number_words in range(len(query_string)+1):
        count_found = base_string.count(query_string[number_words])
        if count_found > 0:
            total_found = total_found + 1
    
    








bible_books = 66 #constant for number of books



#the following code is to cycle through all books, chapters and verse
"""
for index_book in range(1, bible_books+1):
    for index_chapter in range(book_chapters(index_book)+1):
        for index_verse in range(chapter_verses(index_book, index_chapter)+1):
            result_verse = (get_verse(index_book, index_chapter, index_verse))
            

1. take a string to search for - query string
1a. remove punctuation
1b. turn uppercase
2. split it into a list of individual words
3. run a check on all verse to see how many of these list items are present in each verse/turn verse uppercase before compare
4. calculate ratio - number of words in query string *0.6 
5. if 60% words are present, return the string 





"""
def fuzzy_search(query_string):
    query_words = query_string.split()
    query_words = query_string.upper()






"""




source = data["books"][0]["chapters"][0]["verses"][1]["text"]

book = 66
book_index = book - 1
chapter = 5
chapter_index = chapter - 1
verse = 1
verse_index = verse - 1

number_chapters = len(data["books"][book_index]["chapters"])
number_verses = len(data["books"][book_index]["chapters"][chapter_index]["verses"])
print(f"Book: {book}, Chapters in book: {number_chapters}")
print(f"Verse in chapter {chapter}: {number_verses}")

for number in range(number_verses):
    print((data["books"][0]["chapters"][2]["verses"][number]["text"]))
    print(number)
    
    
# Define the pattern to search for
#pattern = input()


# Iterate over the items and perform fuzzy search
for item in data['books']:
    matches = find_near_matches(pattern, item['books'], max_l_dist=1)
    if matches:
        print(f"Found match in item: {item['books']}")
"""