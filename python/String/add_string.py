# Write a python program to add 'ing' at the end of a givan string(length should be at least 3).
# if the givan string already ends with 'ing' then add 'ly' instead if the string length of the givan string
# is less then 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

def add_string(st):
    if len(st) > 2:
        if st.endswith('ing'):
            st += 'ly'
        else:
            st += 'ing'

    print(st)


if __name__ == '__main__':
    add_string('abcing')
    add_string('sting')
    add_string('ab')
