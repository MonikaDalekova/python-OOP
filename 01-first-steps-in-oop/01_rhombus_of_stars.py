n = int(input())


def print_row(size, row): #print in additional function
    print(' '*(size-row), '* '*row)


def upper_part(size): #print first part
    for row in range(1, size+1):
        print_row(size, row)


def lower_part(size): #print second part
    for row in range(size-1, 0, -1):
        print_row(size, row)


def print_rhombus(size): #main function which call the others
    upper_part(size)
    lower_part(size)


print_rhombus(n) #calling the main function

