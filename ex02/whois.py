import sys

if len(sys.argv) == 2:
    i = sys.argv[1]
    if not i.isdigit():
        exit("ERROR")
    i = int(i)
    if i == 0:
        print("Im Zero.")
        sys.exit()
    if (i % 2) == 0:
        print("Im Even.")
    else:
        print("im Odd.")
if len(sys.argv) > 2:
    print("ERROR")