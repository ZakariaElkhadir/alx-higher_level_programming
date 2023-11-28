#!/usr/bin/python3
"""
text must be a string, otherwise raise a TypeError exception with the message text must be a string
There should be no space at the beginning or at the end of each printed line
You are not allowed to import any module
"""

def text_indentation(text):
    """text_indentation fun"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    for delim in ".?:":
        text = (delim + "\n\n").join([line.strip(" ") for line in text.split(delim)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/5-text_identation.txt')