import sys

def shrink(string):
    print(string[:8])

def enlarge(string):
    print(string + 'Z' * (8 - len(string)))


params = sys.argv[1:]

if not params:
    print("none")
else:
    for arg in params:
        if len(arg) < 8:
            enlarge(arg)
        elif len(arg) > 8:
            shrink(arg)
        else:
            print(arg)

