def fourLargest(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return sum(lst[:4])


lst = [1, 1, 3, 2, 5, 4, 1, 0, 9, 1, -5]
r = fourLargest(lst)


def reverse(r):
    st = ""
    for i in str(r):
        st = i + st
    return st


print(reverse(r)+":"+reverse("7hl0q9n8f6b"))
