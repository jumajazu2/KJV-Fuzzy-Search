import json

#from fuzzysearch import find_near_matches 
#some faster libraries here: https://medium.com/codex/best-libraries-for-fuzzy-matching-in-python-cbb3e0ef87dd

# Load the JSON file
with open('C:/Users/Juraj/Documents/IT/Python/KJV_fuzzy_search/kjv.json', 'r') as file:
    data = json.load(file)


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
    try:                #remove articles from string
        query_list.remove("THE")
    except ValueError:
        pass

    try:
        query_list.remove("A")
    except ValueError:
        pass

    return query_list

def compare (query_string, base_string):
    query_string = clean_list(query_string) #turn query string into a list containing its uppercase words, stripped of any punctuation
    #print(query_string)
    base_string = clean_list(base_string) #turn base KJV string into a list containing its uppercase words, stripped of any punctuation
    #print(base_string)
    total_found = 0
    for number_words in range(len(query_string)):
        count_found = base_string.count(query_string[number_words])
        if count_found > 0:
            total_found = total_found + 1
    final_ratio = total_found/len(query_string)

    return(final_ratio)

def scan_all (query_input):
    bible_books = 66 #constant for number of books
    results_verses = [] #create empty list
    for index_book in range(1, bible_books+1):
        for index_chapter in range(book_chapters(index_book)+1):
            for index_verse in range(chapter_verses(index_book, index_chapter)+1):
                base_verse = (get_verse(index_book, index_chapter, index_verse))
                score = compare(query_input, base_verse)
                if score > 0.75:
                    results_verses.append(base_verse)
                    results_verses.append(str(score))
    return results_verses


import pyperclip              
while True:
    query_input = input("String to find: ")
    if query_input == "exit":
        break
    results_verses = scan_all(query_input)
    if len(results_verses) == 0:
        print("No match found.")
    else:
        print(results_verses)
        pyperclip.copy(results_verses[0])



# results could also include context, 5 verses before and after








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






def fuzzy_search(query_string):
    query_words = query_string.split()
    query_words = query_string.upper()










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