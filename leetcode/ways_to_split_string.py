s="abcdabcd"
count=0
for i in range(len(s)):
    s1 = set(s[:i])
    s2 = set(s[i:])
    if len(s1) == len(s2):
        count+=1
print(count)