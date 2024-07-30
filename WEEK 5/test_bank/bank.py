def main():
    str = input("Greeting: ").casefold().strip()
    num = value(str)
    print(f"${num}")

def value(greeting):

    if greeting.startswith('h'):
        if greeting.startswith('hello'):
            n = 0
        else:
            n = 20
    else:
        n = 100

    return n

if __name__ == "__main__":
    main()
