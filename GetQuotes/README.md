# Get Quotes Personal Project

### I read certain Philosophy books and keep track of their quotes. 
### This program allows me to choose these quotes to study on a day-to-day basis and not reuse the same quotes. The script checks if a quote has been reused by using the 'in [file]' statement. If the quote is in the used file, it will not be displayed.
### This is done by importing all the quotes into one .txt file, running the script, and moving those quotes into another .txt file once they have been used.

## Lessons Learned:
1. used.seek(0): I learned the .seek() function which allowed me to specify which line of text to begin searching the text file from. Since it's in a loop, each new loop will restart at line 0.
