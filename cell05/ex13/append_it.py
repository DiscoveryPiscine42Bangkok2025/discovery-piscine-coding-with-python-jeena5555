import sys

param = sys.argv[1:]

if len(param) == 0:
    print("none")
else:
    for word in param:
        if word.endswith("ism"):
            continue
        print(word + "ism")
