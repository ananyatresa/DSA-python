def get_square_sum(n):
    total = 0
    while n>0:
        rem = n%10
        total += rem*rem
        n = n/10
    return total


def is_happy(n):
    result_set = set()
    while n != 1:
        n = get_square_sum(n)
        if n in result_set:
            return False
        else:
            result_set.add(n)
    return True