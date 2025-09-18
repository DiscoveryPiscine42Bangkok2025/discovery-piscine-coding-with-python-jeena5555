import sys

param = sys.argv[1:]

if not param:
    print("none")
else:
    print(f"parameters: {len(param)}")
    for word in param:
        print(f"{word}: {len(word)}")
