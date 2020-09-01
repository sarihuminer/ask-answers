MAX_CHAR = 26
Word = input("enter string \n")
charCount = [0 for i in range(0, MAX_CHAR, 1)]
for i in range(0, len(Word), 1):
    charCount[ord(Word[i]) - ord("a")] += 1
for i in range(0, MAX_CHAR, 1):
    if charCount[i] > 0:
        print(chr(ord("a") + i), end="")
