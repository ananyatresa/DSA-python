# def gray_code(n):
#     # Base case: for n = 0, return an empty list
#     if n == 0:
#         return ['']
#
#     # Recursively get the Gray code for n-1
#     previous_gray_code = gray_code(n - 1)
#     result = []
#
#     # Add '0' to the front of each code from the previous list
#     for code in previous_gray_code:
#         result.append('0' + code)
#
#     # Add '1' to the front of each code from the previous list, in reverse order
#     for code in reversed(previous_gray_code):
#         result.append('1' + code)
#
#     return result
#
#
# print(gray_code(2))
















def gray_code(p, n):
    if len(p) == n:
        return [p]

        # Generate Gray codes by appending '0' and '1'
    result = []
    # Add '0' and '1' recursively with the required order
    result.extend(gray_code(p + '0', n))
    result.extend(reversed(gray_code(p + '1', n)))

    return result


n=2
print(gray_code("", n))