import array as arr

a=arr.array('i', [1, 1])


def fibunachy(n, i):
    if n == 0:
        return
    num = a[i - 1] + a[i - 2]
    a.append(num)
    fibunachy(n - 1, i + 1)


def printarr():
    for num in a:
        print(num)


if __name__ == '__main__':
    fibunachy(5, 2)
    printarr()
