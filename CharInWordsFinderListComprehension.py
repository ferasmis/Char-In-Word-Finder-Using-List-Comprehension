## Author: Feras
## Description: A function that searches a list of words 
##  using list comprehension and uses a key char to find a word and returns a list

def searchString(stringLst, keyword):
    foundKeyWord = [i for i in stringLst for j in i   if j == keyword]
    return foundKeyWord
print(searchString(["rose", "flower", "nice", "light", "beautiful"],"e"))