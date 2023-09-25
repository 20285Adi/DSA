s = input()
stack = []
hm = {")":"(", "]":"[", "}":"{"}
for p in s:
    if p in hm.values():
        stack.append(p)
    elif stack and hm[p] == stack[-1]:
        stack.pop()
    else:
        print('False')

if len(stack) == 0:
    print('True')
elif len(stack) != 0:
    print("false")
