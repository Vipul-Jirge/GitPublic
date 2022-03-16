import re
regex = r"^([a-z|A-Z|0-9|_|-]+)@([a-z|A-Z|0-9]+)\.([a-z|A-Z]+)$"
s = 'fsDZ89-_@ddFF330.extensiontnr'
matches = re.search(regex, s)
if matches == None or len(''.join(matches.groups())) + 2 != len(s):
    print('False')
else :
    print('True')