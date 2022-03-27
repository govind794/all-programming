# Input : Dict = ["go","bat","me","eat","goal","boy", "run"]
#         arr = ['e','o','b', 'a','m','g', 'l']
# Output : go, me, goal.


def count(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict


def possible_words(word_lst, char_lst):
    for i in word_lst:
        flag = 1
        char = count(i)
        for key in char:
            if key not in char_lst:
                flag = 0
            else:
                if char_lst.count(key) != char[key]:
                    flag = 0

        if flag == 1:
            print(i)


if __name__ == "__main__":
    word_lst = ["go", "bat", "me", "eat", "goal", "boy", "run"]
    char_lst = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
    possible_words(word_lst, char_lst)
