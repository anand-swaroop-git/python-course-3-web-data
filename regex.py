# Regular expressions - In computing, a regular expression, also referred to as “regex” or “regexp”, provides a concise and flexible means for matching strings of text, such as particular characters, words, or patterns of characters. A regular expression is written in a formal language that can be interpreted by a regular expression processor.

# Regular Expressions Handout
# ^        Matches the beginning of a line​
# $        Matches the end of the line​
# .        Matches any character​
# \s       Matches whitespace​
# \S       Matches any non-whitespace character​
# *        Repeats a character zero or more times​
# *?       Repeats a character zero or more times (non-greedy)​
# +        Repeats a character one or more times​
# +?       Repeats a character one or more times (non-greedy)​
# [aeiou]  Matches a single character in the listed set​
# [^XYZ]   Matches a single character not in the listed set​
# [a-z0-9] The set of characters can include a range​
# (        Indicates where string extraction is to start​
# )        Indicates where string extraction is to end​

# The regular expressions module
# Before you can use regular expressions in your program, you must import the library using “import re”​
# 
# re.search()
# You can use re.search() to see if a string matches a regular expression, similar to using the find() method for strings​
# 
# 
#re.findall() 
#You can use re.findall() to extract portions of a string that match your regular expression, similar to a combination of find() and slicing:  var[5:10]

# Using re.search() Like find()​
#     First using the find() method
# hand = open('mbox-short.txt')​
# for line in hand:​
#     line = line.rstrip()​
#     if line.find('From:') >= 0:​
#         print(line)​

#     Now using the re.search() function
# import re​
# hand = open('mbox-short.txt')​
# for line in hand:​
#     line = line.rstrip()​
#     if re.search('From:', line) :​
#         print(line)​

# Using re.search() Like startswith()​
#     First using startswith
# hand = open('mbox-short.txt')​
# for line in hand:​
#     line = line.rstrip()​
#     if line.startswith('From:') :​
#         print(line)​
    
#     Now using re.search() function in re library
# import re​
# hand = open('mbox-short.txt')​
# for line in hand:​
#     line = line.rstrip()​
#     if re.search('^From:', line) :​
#         print(line)​


# Fine-Tuning Your Match​ - /S is - Match any non-whitespace character
# ^X-\S+:​