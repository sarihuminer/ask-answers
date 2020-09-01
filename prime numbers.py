import math
import array as arr


def prime_numbers(n):
    a = arr.array("i")
    for i in range(2, n):
        m = int(math.sqrt(i))
        for j in range(2, i):
            if i % j == 0:
                break
            a.append(i)
            break
    for n in a:
        print(n, end=" ")


prime_numbers(1000)
