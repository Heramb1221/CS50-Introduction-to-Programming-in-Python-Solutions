def main():

    i = (input("Fraction: ")).strip()
    per = convert(i)
    oupt = gauge(per)

    print(oupt+"%")


def convert(fraction):
    try:
        x , y = fraction.split('/')

        if int(x) > int(y):
            raise ValueError

        f = round((int(x)/int(y))*100)
        return int(f)
    except (ValueError, ZeroDivisionError):
        print("Error")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage)


if __name__ == "__main__":
    main()
