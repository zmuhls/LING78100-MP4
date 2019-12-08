MP4: Regular expressions
========================

This MP consists of two parts, both using Python's `re` module.

Matching
--------

Download the attached [`wordlist.txt`](wordlist.txt) file. Each line contains an
English word. Open the file in Python, and read the words line by line. For
each word, if the word contains any "doubled" (i.e., repeated and adjacent)
letters, print it out; otherwise, do not print it. For instance, you would
print the word *annoy* because it contains the subsequence *nn*, but not
*suds* because the two _s_ characters are not adjacent.

### What to turn in

-   A code snippet which performs the requested operation

### Hints

-   There is more than one way to solve this.
-   Don't forget to strip your lines; don't print any blank lines.
-   You will want to use `re.search` rather than `re.match` (ask yourself why).
-   You may wish to consult [the documentation for
    `re.search`](https://docs.python.org/3/library/re.html#re.search).
-   You do not need to write a class or a function here, though a simple
    function might be a helpful way to "encapsulate" your code.

### Test support

There are 197 words (or 195 unique words) with doubled letters in the wordlist;
the first being *bottler* and the last being *volunteers*. You may want to keep
track of the number of words with doubled letters to test your solution.

Substitution
------------

Often when dealing with corpus data, we wish to remove
[personally identifying information (PII)](https://en.wikipedia.org/wiki/Personal_data).
Using the following `corpus` string, write regular expressions that find all
instances of complete 7-, 11, and 13-digit phone numbers and rewrite them so that
every digit is a 0. For example, _345-6789_ is a 7-digit phone number, and
_044-113-496-0000_ is a 13-digit number.

```python
corpus = """In the US, some phone numbers are reserved for fictitious purposes.
For instance, 555-0198 and 1-206-5555-0100 are example fictitious numbers.
There are similar ranges of numbers in the UK, Ireland, and Australia.
In the UK, 044-113-496-1234 is a fictitious number in the Leeds area.
In Ireland, the number 353-020-913-1234 is fictitious.
And in Australia, 061-900-654-321 is a fictitious toll-free number.
911 is a joke."""
```

### What to turn in

-   A code snippet which performs the requested substitution
-   An assertion test confirming the correctness of your code

### Hints

-   There is more than one way to solve this.
-   You will **not** receive full credit if you instead use functions like
    `str.replace`.
-   You do not need to write a class or a function here, though a simple
    function might be a helpful way to "encapsulate" your code.
