import math
import array as arr

def prime_numbers(n):
    # Corner case
    b = arr.array("i", [2])
    for i in range(3, n):
        prime = True
        if (i <= 1):
            continue
        # Check from 2 to n-1
        for j in range(2, i):
            if (i % j == 0):
                prime = False
                break
        if prime == True:
            b.append(i)

        # b.append(i)
    for i in b:
        print(i, end=" ")


if __name__ == '__main__':
    prime_numbers(30)
# This code is contributed by Sachin Bisht
