d = {}

while True:
    try:
        items = input().upper()

    except EOFError:
        break
    else:
        if items in d:
            d[items] += 1
        else:
            d[items] = 1

for i in sorted(d):
    print(f"{d[i]} {i}")
