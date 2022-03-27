from collections import Counter


# def winner(lst):
#     dic = Counter(lst)

#     dict = {}

#     for value in dic.values():
#         dict[value] = []

#     for key, value in dic.items():
#         dict[value].append(key)

#     maxVote = sorted(dict.keys(), reverse=True)[0]

#     # print(maxVote)

#     if len(dict[maxVote]) > 1:
#         print(sorted(dict[maxVote])[0])
#     else:
#         print(dict[maxVote][0])


#     # print(dict)


def winner(lst):
    voter = Counter(lst)
    print(voter)
    max_voter = max(voter.values())
    r = [i for i in voter.keys() if voter[i] == max_voter]

    # print(sorted(r)[0])


if __name__ == "__main__":
    lst = ['johnny', 'jackie',
           'john', 'jackie', 'jamie', 'jamie',
           'john', 'johnny', 'jamie', 'johnny',
           'john']
    winner(lst)
