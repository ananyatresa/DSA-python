def target_sum(p, up, target, memo=None):

    # Calculate the current index and current sum to use as a key
    index = len(p)
    current_sum = sum(p)

    # Check if we reached the end of the list
    if len(up) == 0:
        return 1 if current_sum == target else 0

    # Check if the result is already in the memo
    if (index, current_sum) in memo:
        return memo[(index, current_sum)]

    # Recursive case - Add '+' char
    count = target_sum(p + [up[0]], up[1:], target, memo)

    # Recursive case - Add '-' char
    count += target_sum(p + [-up[0]], up[1:], target, memo)

    # Memoize the result before returning
    memo[(index, current_sum)] = count
    return count


nums=[1,1,1,1,1]
target=3
print(target_sum([], nums, target))
