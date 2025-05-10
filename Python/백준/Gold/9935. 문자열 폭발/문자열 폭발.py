string = input()
boom = input()
a = len(boom)

res = []
for s in string:
    res.append(s)
    if ''.join(res[-a:]) == boom:
        del res[-a:]

if len(res) == 0:
    print('FRULA')
else:
    print(''.join(res))