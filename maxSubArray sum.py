a = [-2, -3, 4, -1, -2, 1, 5, -3]


def find_max_sub_array(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for item in arr:
        max_ending_here = max(item, max_ending_here + item)
        max_so_far = max(max_so_far, max_ending_here)
    print(max_so_far)


def find_max_sub_array_and_index(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    start = end = s = 0
    for i in range(len(arr)):
        max_ending_here += arr[i]
        if arr[i] > max_ending_here:
            max_ending_here = arr[i]
            start = i
            end = i
            s = i
        if max_so_far < max_ending_here:
            start = s
            max_so_far = max_ending_here
        else:
            end += 1

    print(max_so_far)
    print("start {} end {}".format(str(start), str(end)))


if __name__ == '__main__':
    find_max_sub_array(a)

    find_max_sub_array_and_index(a)
