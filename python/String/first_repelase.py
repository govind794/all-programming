# Write a python program to get a string from a givan string where all occurrences of
# its first char have been changed '$', except the first char itself
# Simple String = "restart"
# Expected result = "resta$t"

st = "restart"
# st1 = []
# for i in st:
#     if i == st[:1]:
#         st1.append("$")
#     else:
#         st1.append(i)

# print(st[:1] + "".join(st1[1:]))

char = st[:1]
st = st.replace(char, "$")
print(char + st[1:])
