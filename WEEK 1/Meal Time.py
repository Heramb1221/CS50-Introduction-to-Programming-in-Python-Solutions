def main():
    str = input("What time is it? ")
    x = convert(str)

    if 7 <= x <=  8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    y = float(hours)+((float(minutes)/60))
    return y


if __name__ == "__main__":
    main()