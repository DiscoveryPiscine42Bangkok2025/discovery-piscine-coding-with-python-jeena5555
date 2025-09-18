import sys

if len(sys.argv) != 2:
    print("none")
else:
    param = sys.argv[1]
    result = ""

    for char in param:
        if char == 'z':
            result += 'z'

    if result != "":
        print(result)
    else:
        print("none")
