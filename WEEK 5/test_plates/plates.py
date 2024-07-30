def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #for lengths
    if len(s) < 2 or len(s) > 6:
        return False

    #to check for spaces etc
    if not s.isalnum():
        return False

    if not s[0:2].isalpha():
        return False

    #to get index of number
    s2 = ''
    for i in range(len(s)):
        if s[i].isdigit():
            s2 = s[i-1:len(s)]

    #check s2 is all numbers
    for i in range(len(s2)):
        if not s2[i].isdigit():
                return False

        elif s2[i].isdigit():
            if s2[0] == '0':
                return False
        else:
            return True

    return True

if __name__ == "__main__":
    main()
