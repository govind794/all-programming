from collections import OrderedDict


def distinct(lst):
    order = OrderedDict.fromkeys(lst)
    print(order)
    result = [key for (key, value) in order.items()]

    print(', '.join(map(str, result)))

if __name__ == "__main__":
    lst = [12, 3, 5, 12, 4, 3]
    distinct(lst)