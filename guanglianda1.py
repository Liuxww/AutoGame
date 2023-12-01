string = "aab"

import copy
flag = 0
i = 0
while string:
    i = 0
    temp = copy.deepcopy(string)
    while i < len(string)-1:
        if string[i] == string[i+1]:
            string = string[:i] + string[i+2:]
            flag ^= 1
        else:
            i += 1
    if temp == string:
        break
if flag:
    print('Yes')
else:
    print('No')