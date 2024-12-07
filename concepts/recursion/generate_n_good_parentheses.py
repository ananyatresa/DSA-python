def generateCombinations(p, open_count, close_count):
    # If the p string has reached the desired length (2 * n)
    n=3
    if len(p) == 2 * n:
        return [p]

    result = []

    # Add an open parenthesis if we still have remaining '(' to add
    if open_count < n:
        result.extend(generateCombinations(p + "(", open_count + 1, close_count))

    # Add a close parenthesis if it would not make the string invalid
    if close_count < open_count:
        result.extend(generateCombinations(p + ")", open_count, close_count + 1))

    return result



n=3
print(generateCombinations("", 0,0))
