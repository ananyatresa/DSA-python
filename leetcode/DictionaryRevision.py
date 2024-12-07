##7 Count occurencesof all elements in a list:-
# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# result = dict()
# for number in numbers:
#     if result.get(number):
#         result[number] += 1
#     else:
#         result[number] = 1
# print(result)

##8 Calculate sum of all values in a dictionary:-
# data = {'a': 10, 'b': 20, 'c': 30}
# result = 0
# print(sum(data.values())
# OR
# for value in data.values():
#     result += value
# print(result)

##9 Create a new dict with only even values:-
# data = {'a': 10, 'b': 21, 'c': 30}
# new_dict = dict()
# for key, value in data.items():
#     if value % 2 == 0:
#         new_dict[key] = value
# print(new_dict)
##    OR
# print({k:v for k,v in data.items() if v%2 == 0})


# 10 Mapping Squares:-

# numbers = [1, 2, 3, 4]
# print ({k:k*k for k in numbers})


# 11 Grouping by remainder:-

# numbers = [1, 2, 3, 4, 5, 6]
# divisor = 3
# result_dict = dict()
# for num in numbers:
#     rem = num % divisor
#     if result_dict.get(rem):
#         result_dict[rem].append(num)
#     else:
#         result_dict[rem] = [num]
# print(result_dict)


# 12 Given a number n, you need to find all its divisors:-

# n = 36
# # Output: [1, 2, 4, 7, 14, 28]
# result = list()
# for num in range(1, n + 1):
#     if n % num == 0:
#         result.append(num)
# print(result)


##13 Chefs Birthday Cakes

# avail = {'flour': 1000, 'sugar': 500, 'eggs': 10, 'milk': 2000, 'tomatoes': 6}
#
# # Recipe for one cake
# recipe = {'flour': 250, 'sugar': 200, 'eggs': 2, 'milk': 500}

# result = dict()
# for k,v in recipe.items():
#     if avail.get(k):
#         result[k] = avail[k]//v
# print(min(result.values()))

##   OR

# print(min(avail.get(k, 0) // v for k, v in recipe.items()))


#14 Count words in a string