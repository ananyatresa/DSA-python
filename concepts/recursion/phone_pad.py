def phone_pad(p, up):
    if len(up) == 0:
        return [p] if p != "" else []

    arr = []
    digit = up[0]
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    letters = phone_map[digit]
    for i in letters:
        arr.extend(phone_pad(p + i, up[1:]))

    return arr


print(phone_pad("", "23"))
