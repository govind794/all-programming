# Write a python program to get a string made of the first 2 and
# the last 2 chars from a givan string.
# if a string length is less then 2 return instead of the empty string.

# Simple string = "w3resource"
# Expected result = "w3ce"
# Simple string = "w3"
# Expected result = "w3w3"

st = "w3resource"
# st = "w"
size = len(st)

if size > 1:
    print("".join(st[:2] + st[-2:]))
else:
    print("Empty string")
