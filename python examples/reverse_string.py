import re
name = input()
str = ''
piece = name.split()
if piece == 1:
    print('Error')
else:
    for i in name:
        str = i + str
    print(str)
