import json
import asyncio
from rich import print
from rich.console import Console

#from fuzzysearch import find_near_matches 
#some faster libraries here: https://medium.com/codex/best-libraries-for-fuzzy-matching-in-python-cbb3e0ef87dd

# terminal display fromatting https://rich.readthedocs.io/en/stable/index.html

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

def get_reference (book_no, chapter_no, verse_no):  #return a specific verse
    book_index = book_no - 1
    chapter_index = chapter_no - 1
    verse_index = verse_no -1

    reference = (data["books"][book_index]["chapters"][chapter_index]["verses"][verse_index]["name"])

    return reference

def clean_list (query_string):
    query_string = query_string.upper() #make whole string uppercase
    mydict = {46: None, 44: None, 59: None, 63: None, 34: None, 45: None, 33: None, 34: None, 62: None, 60: None, 47: None} # remove . , ; ? " -
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

    try:
        query_list.remove("#KJVFS#")
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
    try:
        final_ratio = total_found/len(query_string)
    except ZeroDivisionError:
        final_ratio = 0

    return(final_ratio)

def scan_all (query_input):
    bible_books = 66 #constant for number of books
    results_verses = [] #create empty list
    number_results = 0
    for index_book in range(1, bible_books+1):
        for index_chapter in range(book_chapters(index_book)+1):
            for index_verse in range(chapter_verses(index_book, index_chapter)+1):
                base_verse = (get_verse(index_book, index_chapter, index_verse))
                score = compare(query_input, base_verse)
                if score > 0.75:
                    ref = get_reference(index_book, index_chapter, index_verse)
                    results_verses.append(ref)
                    results_verses.append(base_verse)
                    results_verses.append(str(score))
                    results_verses.append("----------------------------------------------------------------")
                    number_results = number_results + 1
    print("Number of hits:")
    print(number_results)
    print("\n")
    return results_verses


import pyperclip   

launch_code = "#KJVFS#"

original_content = ""

async def check_clipboard():
    while True:
# Get the current clipboard content
        clipboard_content = pyperclip.paste()

# Check if the specific text is in the clipboard
        global original_content
        if clipboard_content != original_content:
            #print("Launch code detected in clipboard!")
            
            #console = Console()
            #console.clear()
            #print(clipboard_content)
            original_content = clipboard_content
            await execute_code(clipboard_content)
            

# Wait for a short period before checking again
        await asyncio.sleep(1)

async def execute_code(clipboard_content):
# Your code to execute when the specific text is found
    clipboard_content_cleared = clipboard_content #.translate(str.maketrans('', '', '#KJVFS#')) 
    #print(clipboard_content_cleared)
    #pyperclip.copy('')
    
    results_verses = scan_all(clipboard_content_cleared)
    if len(results_verses) == 0:
        #console = Console()
        #console.clear()
        print("No match found.")
    else:
        for item in range(int(len(results_verses))):
            #print(item)
            print(results_verses[item])
            #print("\n")
        #pyperclip.copy(results_verses[0])


# Start monitoring the clipboard

#console = Console()
#console.clear()
print("Monitoring clipboard...")
asyncio.run(check_clipboard())





# results could also include context, 5 verses before and after

# sorting results by score

# automatic look when a segment is selected

# indicate differences, show context in dart

# another button to send the whole segment to search
