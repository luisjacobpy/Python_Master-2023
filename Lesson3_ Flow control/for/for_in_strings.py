'''
For in Strings
'''
string1 = 'hello my friend!'
for character in string1:
    print(character)

'''
I what add character * in the string
'''
string2 = ''
string3 = ''
for character in string1:
    print(character)
    string2 += "*"
    string3 += character * 2
print(string1)
print(string2)
print(string3)
