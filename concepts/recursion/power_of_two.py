def power_of_two(n):
    if n == 1:
        return True
    if n % 2 != 0 or n == 0:
        return False
    return power_of_two(n//2)


print(power_of_two(1))
# O(logN)

# Better non recursive solution--> using bitwise trick that brings TC to O(1)
# (n & (n-1)) == 0 => Condition true only for power of 2 cases.
# return n>0 and (n & (n-1)) == 0


