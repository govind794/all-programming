# Write a python program to count the number of characters in a string.
# Simple string = "google.com"
# Expected result = {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.':1, 'c': 1, 'm': 1}

import collections 

st = "google.com"

# result = collections.Counter(st)
# print(result)
dic = {}

for i in st:
    try:
        dic[i] += 1
    except:
        dic[i] = 1

print(dic)