# Write a python program to get a single string from two givan string, separated by a space
# and swap a first two char of each string
# Simple string = "abc", "xyz"
# Expected result = "xyc", "abz"

# st = "abc", "xyz"

# print(st[1][:2] + st[0][-1:])
# print(st[0][:2] + st[1][-1:])


def char_swap(a, b):
    x = b[:2] + a[2:]
    y = a[:2] + b[2:]
    
    return x + " " + y


if __name__ == "__main__":
    print(char_swap("abc", "xyz"))
