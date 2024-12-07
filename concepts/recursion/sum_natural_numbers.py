def sum(n):
    return 1 if n==1 else n + sum(n-1)

print(sum(7))