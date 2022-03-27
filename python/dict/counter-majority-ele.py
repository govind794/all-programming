from collections import Counter


def mejority(lst):
    freDict = Counter(lst)
    size = len(lst)
 
    for key, value in freDict.items():
        if value > (size//2):
            print(key)
            return
    print("None")


if __name__ == "__main__":
    lst = [3, 3, 4, 2, 4, 4, 2, 2,2,2,2]
    mejority(lst)
