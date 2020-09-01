arr = [4, 12, 5, 18, 2, 4, 20, 1]
sum = max = 0
min = minPeriod = arr[0]

for num in arr:
    if num - minPeriod > sum:
        min = minPeriod
        sum = num - min
        max = num
    elif sum < 0:
        minPeriod = num
    if num < min and num < minPeriod:
        min = minPeriod
        minPeriod = num
print("min is {} max is {} sum is {}".format(min, max, sum))
