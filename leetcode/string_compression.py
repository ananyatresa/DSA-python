chars = ['a','a','b','b','a','a','c','c','c','c','c','c','c','c','c','c','c','c']

i = 0
prev_char = ''
group = 1
s=''
for i in range(len(chars)):
    ch = chars[i]

    if prev_char == ch:
        group += 1
    else:
        if group == 1:
            s += prev_char
        else:
            s = s + prev_char + str(group)
        prev_char = ch
        group = 1

if group == 1:
    s += prev_char
else:
    s = s + prev_char + str(group)


chars = list(s)
print(chars)