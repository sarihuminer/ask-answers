def find_elements(arr, sum):
    myDict = {}
    for num in arr:
        myDict[sum - num] = ""
    n = arr[0]
    i = 0
    while n != " ":
        if n in myDict.keys():
            return "yes", n
        i += 1
        n = arr[i]


if __name__ == "__main__":
    arr = [2, 5, 4, 87, 9, 654, 45, 5, 8, 2, 3, 58, 2, 7]
    b, n = find_elements(arr, 712)
    print("{} the number is : {} {}".format(b, n, 712 - n))
