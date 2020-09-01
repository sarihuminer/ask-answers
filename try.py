x = ""
while x == "":
    x = input("enter your name \n")
    if int(x):
        print("eror! enter name not integer!")
    elif x != "":
        print("hellow {}".format(x), end="\n")
    else:
        print("eror!")
