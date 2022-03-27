# Write a python function that takes a list of words and return the
# longest word and lenght of the longest one
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

from operator import itemgetter


def longest_word(st):
    lst = [{i: len(i)} for i in st]
    d = {}
    for i in lst:
        d.update(i)

    for key, value in sorted(d.items(), key=itemgetter(1), reverse=True):
        print('Longest word: ', key)
        print('Length of the longest word: ', value)
        break


if __name__ == '__main__':
    st = "My name is govind patidar"
    longest_word(st.split())
