x = "global" #1


def outer():
    x = "local"

    def inner():
        nonlocal x # connect inner x with x = "local"
        x = "nonlocal"
        print("inner:", x) #3

    def change_global():
        global x
        x = "global: changed!" #5 here

    print("outer:", x) #2
    inner() #3
    print("outer:", x) #4 here
    change_global()


print(x)
outer()
print(x)