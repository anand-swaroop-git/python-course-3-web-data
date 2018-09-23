# ASCII - American Standart Code for Information Interchange
# Representing Simple Strings
# Each character is represented by a number between 0 and 256 stored in 8 bits of memory
# We refer to these 8 bits of memory as a "byte" of memory


# The ord() function tells us the numeric value of a simple ASCII character
# print(ord('H'))

# Multi-Byte Characters​
# To represent the wide range of characters computers must handle we represent characters with more than one byte​
# UTF-16 – Fixed length - Two bytes​
# UTF-32 – Fixed Length - Four Bytes​
# UTF-8 – 1-4 bytes​
#     Upwards compatible with ASCII​
#     Automatic detection between ASCII and UTF-8​
#     UTF-8 is recommended practice for encoding data to be exchanged between systems​

# Two Kinds of Strings in Python​
#     In Python 2.7.10 ​
#     >>> x = '이광춘'​
#     >>> type(x)​
#     <type 'str'>​
#     >>> x = u'이광춘'​
#     >>> type(x)​
#     <type 'unicode'>​
#     >>> ​

#     In Python 3.5.1​
#     >>> x = '이광춘'​
#     >>> type(x)​
#     <class 'str'>​
#     >>> x = u'이광춘'​
#     >>> type(x)​
#     <class 'str'>​
#     >>> ​

# Python 3 and Unicode​
# In Python 3, all strings internally are UNICODE ​
# Working with string variables in Python programs and reading data from files usually "just works"​
# When we talk to a network resource using sockets or talk to a database we have to encode and decode data (usually to UTF-8)​

# On the way out, we have a internal string. Before we send it, we have to encode it, and then we send it. Getting stuff back, we receive it, it comes back as bytes. We happen to know it's UTF-8 or we're letting it automatically detect UTF-8 and decode it and now we have a string. And now internally inside of Python we can write files, we can do all kinds of stuff in and out of stuff and it sort of works all together. 

# Network Programs
# Using urllib in Python
# Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file​

# import urllib.request
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

# Treating webpages like a file and counting the words in that file
# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

# Finding hrefs from an HTML file | Following links
# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fhand:
#     print(line.decode().strip())

# BeautifulSoup installation on Windows
# https://www.youtube.com/watch?v=FdDakO9fPLw
# We use the following test URLs to test the below script
# http://www.dr-chuck.com/page2.htm
# http://www.dr-chuck.com/page1.htm
# The below script gives us all the anchor tags in a webpage using BeautifulSoup library
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

# web-crawler with SSL ignore with BeautifulSoup
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

# Assignment 1st of week 4 (WIP)
# http://py4e-data.dr-chuck.net/comments_42.html
import urllib.request
import re
fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html')
for line in fhand:
    x = (line.decode().strip())
    # print(x)
    for line in x:
        y = re.findall('[0-9]+',line)
        if y != 
        print(y)