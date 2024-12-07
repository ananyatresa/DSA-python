arr = [10, 10, 3, 4, 10]

arr.sort()
#  1 2 3 9 10 10
min_amp = arr[len(arr) -1]
# There are 3 options:
# remove 3 from end
# remove 2 from end and 1 from start
# remove 1 from end and 2 from start
# remove 3 from start
min_amp = min(min_amp, arr[-4] - arr[0])
min_amp = min(min_amp, arr[-3] - arr[1])
min_amp = min(min_amp, arr[-2] - arr[2])
min_amp = min(min_amp, arr[-1] - arr[3])
print(min_amp)