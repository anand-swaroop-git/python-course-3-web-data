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
# The above regular expression will return a false for this line - X-Plane is behind schedule: two weeks

# Extracting Data using Python
# Matching and Extracting Data
    # re.search() returns a True/False depending on whether the string matches  the regular expression
    # If we actually want the matching strings to be extracted, we use re.findall()

# >>> import re
# >>> x = 'My 2 favorite numbers are 19 and 42'
# >>> y = re.findall('[0-9]+',x)
# >>> print(y)
# ['2', '19', '42']

# Searching for the strings using re.findall
# >>> import re
# >>> x = 'My 2 favorite numbers are 19 and 42'
# >>> y = re.findall('[0-9]+',x)
# >>> print(y)
# ['2', '19', '42']
# >>> y = re.findall('[AEIOU]+',x)
# >>> print(y)
# []

# Greedy Matching
# >>> import re
# >>> x = 'From: Using the : character'
# >>> y = re.findall('^F.+:', x)
# >>> print(y)
# ['From: Using the :']

# Non-Greedy Matching
# >>> import re
# >>> x = 'From: Using the : character'
# >>> y = re.findall('^F.+?:', x)
# >>> print(y)
# ['From:']

# Extracting Email using regex
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# >>> y = re.findall('\S+@\S+',x)
# >>> print(y)
# ['stephen.marquard@uct.ac.za’]

# Fine-Tuning String Extraction
# Parentheses are not part of the match - but they tell where to start and stop what string to extract
# x= From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# >>> y = re.findall('\S+@\S+',x)
# >>> print(y)
# ['stephen.marquard@uct.ac.za']
# >>> y = re.findall('^From (\S+@\S+)',x)
# >>> print(y)
# ['stephen.marquard@uct.ac.za']

# String Parsing Examples
# We want to extract uct.ac.za from the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#     Old Program in earlier classes:
# >>> data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# >>> atpos = data.find('@')
# >>> print(atpos)
# 21
# >>> sppos = data.find(' ',atpos)
# >>> print(sppos)
# 31
# >>> host = data[atpos+1 : sppos]
# >>> print(host)
# uct.ac.za
#     Another program using the double-split method
# words = line.split()
# email = words[1]
# pieces = email.split('@')
# print(pieces[1])
#     The regular expression method
# import re 
# lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('@([^ ]*)',lin)
# print(y)
# ['uct.ac.za']

# So in the above regex example, we are using the following regex to find out the domain name of the email address:
# re.findall('@([^ ]*)',lin)
# re.findall('^From .*@([^ ]*)',lin)

# So, now we have to search for floating point numbers from the this format X-DSPAM-Confidence: 0.8475
# import re
# hand = open('mbox-short.txt')
# numlist = list()
# for line in hand:
#     line = line.rstrip()
#     stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
#     if len(stuff) != 1 :  continue
#     num = float(stuff[0])
#     numlist.append(num)
# print('Maximum:', max(numlist))

# Escape character
# >>> import re
# >>> x = 'We just received $10.00 for cookies.'
# >>> y = re.findall('\$[0-9.]+',x)
# >>> print(y)
# ['$10.00']

# Assignment - Finding Numbers in a Haystack
# import re
# add = 0
# file = open('regex_sum_133477.txt', 'r')
# for line in file:
#     numbers = re.findall('[0-9]+', line)
#     if not numbers: continue
#     else:
#         for number in numbers:
#             add = add + int(number)
# print(add)
















