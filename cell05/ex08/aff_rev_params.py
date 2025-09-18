import sys

param = sys.argv[1:]

if len(param) < 2:
    print("none")
else:
    for word in reversed(param):
        print(word)
