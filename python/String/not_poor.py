# Write a Python program to find the first appearance of the substring 'not' and 'poor'
# from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
#  substring with 'good'. Return the resulting string. Go to the editor

# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def not_poor(st):
    snot = st.find('not')
    spoor = st.find('poor')

    if spoor > snot and snot > 0 and spoor > 0:
        return st.replace(st[snot:(spoor+4)], 'good')
    else:
        return st


# st = 'The lyrics is not that poor!'
st = 'The lyrics is poor!'

print(not_poor(st))
