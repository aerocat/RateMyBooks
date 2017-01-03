# RateMyBooks

<i>tl;dr
A simple Python script that given a .txt file of a list of books and, using the GoodReads API, returns a list of the books sorted by rating (descending order).
</i>

## The idea:
Over the years, I've kept a list of books that I hope someday to read. Whenever I get a recommendation, I add it to my list.

One night, I decided I wanted to start reading a new book. However, I quickly realized that my list had become very long (80+ books), and I had no criteria to sort it. There were books from so many different genres, and some had obscure titles I didn't even remember adding. I thought it would've been great if I had the list sorted by some criteria like rating: even though rating can be very subjective, it could have given me a starting point to choose which book to read!

So, I spent the next 2 hours writing this script. I hadn't used Python in a while so I kept googling stuff like proper syntax or basic functions :P, nonetheless I was pretty proud when I finished it.

## How to use it:
0. Requirements:
If you don't have them already, you need to install the two Python modules BeautifulSoup and lxml. Using pip:
<code> pip install beautifulsoup4 lxml </code>
1. Download or save the rate_my_books.py file
2. Acquire an API key from http://goodreads.com/api and insert it between the single quotes at line 25
3. Have your list of books in a .txt files, one per line, and place it in the sample folder of the script.
4. Simply run the script, it will ask you for the name of the file of your list.

## Example:
<pre>
<code> $ python rate_my_books.py 
Enter filename of the list of books: your_list.txt
1 books processed out of 3. (1 book/sec)
2 books processed out of 3. (1 book/sec)
3 books processed out of 3. (1 book/sec)
Here is the resulting ranking based on your book list!

4.10	War and Peace, Leo Tolstoy (1865)
3.80	A Tale of Two Cities, Charles Dickens (1859)
3.75	Zen and the Art of Motorcycle Maintenance: An Inquiry Into Values, Robert M. Pirsig (1974)
</code>
</pre>
