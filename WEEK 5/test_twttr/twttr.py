def main():
    str = input("Input: ")
    oupt = shorten(str)

    print(oupt)


def shorten(word):
    v = ['a','e','i','o','u','A','E','I','O','U']

    omi = ""

    for letters in word:
        if letters in v:
            pass
        else:
            omi += letters

    return omi

if __name__ == "__main__":
    main()
