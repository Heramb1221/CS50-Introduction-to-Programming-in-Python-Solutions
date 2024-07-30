def main():
    f = get_int()
    print_out(f)

def get_int():
    while True:
        try:
            i = (input("Fraction: ")).strip()
            x , y = i.split('/')

            if int(x) > int(y):
                raise ValueError

            f = round((int(x)/int(y))*100)
            return int(f)
        except (ValueError, ZeroDivisionError):
             pass

def print_out(n):
    if n <= 1:
        print("E")
    elif n >= 99:
        print("F")
    else:
        print(f"{n}%")

main()
