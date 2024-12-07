def roman_to_int(str):
    dict_roman = {"I":1,"V":5, "X":10, "L":50, "C":100, "D": 500, "M":1000}
    result = 0
    for i in range(len(str)):
        if i < len(str) - 1 and dict_roman[str[i]] < dict_roman[str[i+1]]:
            result -= dict_roman[str[i]]
        else:
            result += dict_roman[str[i]]
    return result





# str="III"
# str="MCMXCIV"
str="IV"
print(roman_to_int(str))