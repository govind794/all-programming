# Input  : str = “xyyz”
# Output : Yes
# We can remove character ’y’ from above
# string to make the frequency of each
# character same.

from collections import Counter


def same(st):
    dict = Counter(st)

    r = list(set(dict.values()))

    print(r)

    if len(r) > 2:
        print("No")
    elif len(r) == 2 and r[1]-r[0] > 1:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    st = "xyyzzz"
    same(st)
