rooms = ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]

hmap={}
for i in rooms:
    room = i[1:]
    if i.startswith("+"):
        hmap[room] = hmap.get(room, 0) + 1

print(min(hmap, key=lambda x: (-hmap[x], x)))