number_stack = []
max_stack = []


def insert(num):
    if len(max_stack) == 0:
        max_stack.append(num)
    elif max_stack[0] < num:
        max_stack.insert(0, num)
    number_stack.insert(0, num)


def pop():
    numpop = number_stack.pop(0)
    if numpop == max_stack[0]:
        max_stack.pop(0)


def max():
    print(max_stack[0])


def MYprint(arr):
    for x in arr:
        print(x, end=" ")
    print("\n")


if __name__ == '__main__':
    insert(4)
    insert(3)
    insert(8)
    insert(9)
    MYprint(number_stack)
    MYprint(max_stack)
    pop()
    max()
    MYprint(number_stack)
    MYprint(max_stack)
    pop()
    max()
    MYprint(number_stack)
    MYprint(max_stack)
