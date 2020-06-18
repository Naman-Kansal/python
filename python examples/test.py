largest = None
smallest = None
while True:
    num = input("Enter a number(Enter done to exit): ")
    exit_loop = ['done', 'don', 'do', 'd', 'yes', 'ye', 'y']
    if num in exit_loop:
        break

    try:
        fval = float(num)
    except ('SyntaxError'):
        print("Invalid input")
        continue

    if largest is None:
        largest = fval
    elif fval > largest:
        largest = fval
    if smallest is None:
        smallest = fval
    elif fval < smallest:
        smallest = fval
    # for fval in range(1, 10, 2):
    #     print(fval)
print("Maximum is", largest)
print("Minimum is", smallest)
