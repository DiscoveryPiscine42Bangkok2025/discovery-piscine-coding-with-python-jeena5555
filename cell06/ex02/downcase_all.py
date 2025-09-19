import sys

def downcase_it(text):
    return text.lower()

params = sys.argv[1:]

if not params:
    print("none")
else:
    for arg in params:
        print(downcase_it(arg))
