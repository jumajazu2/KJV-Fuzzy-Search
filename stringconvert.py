query_string = "I am, very, special;, item. where?"

query_words = query_string.upper()
mydict = {46: None, 44: None, 59: None, 63: None, 34: None, 45: None} # remove . , ; ? " -
query_words = query_words.translate(mydict)

#print(query_words)
query_words = query_words.split()
#print(query_words)

print (query_words)

"""

test = query_words[1]
adjusted = test.translate(mydict)

print (adjusted)
for index in range(len(adjusted))
query_words[1] = query_words[1].translate(mydict)
print(query_words[1])

"""