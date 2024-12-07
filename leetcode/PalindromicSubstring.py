input_str = "noon"
result = 0
for i in range(len(input_str)):
    for j in range(i, len(input_str)):
        original = input_str[i:j+1]
        reverse = input_str[i:j+1][::-1]
        print(f" Original: {original} and Reversed: {reverse}")
        if original == reverse:
            result += 1
            print("Found Palindrome!")
print(result)
