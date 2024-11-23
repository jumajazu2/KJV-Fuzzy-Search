import json

from fuzzysearch import find_near_matches 


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

def book_chapters(book_no):
    book_index = book_no - 1
    number_chapters = len(data["books"][book_index]["chapters"])
    #number_verses = len(data["books"][book_index]["chapters"][number_chapters-1]["verses"])
    return number_chapters

def chapter_verses(book_no, chapter_no):
    book_index = book_no - 1
    chapter_index = chapter_no - 1
    number_verses = len(data["books"][book_index]["chapters"][chapter_index]["verses"])
    return number_verses

print(book_chapters(5))
print(chapter_verses(5, 8))

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