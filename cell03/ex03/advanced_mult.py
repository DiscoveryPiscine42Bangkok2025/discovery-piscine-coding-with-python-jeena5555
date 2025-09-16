import sys

if len(sys.argv) > 1:
    print("none")
else:
    table = 0
    while table <= 10:
        print(f"Table de {table}:", end=" ")
        multi = 0

        while multi <= 10:
            print(table * multi, end=" ")
            multi += 1
            
        print()
        table += 1
