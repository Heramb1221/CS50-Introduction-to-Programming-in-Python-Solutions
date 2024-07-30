import re

def main():
    print(count(input("Text: ")))


def count(s):
    um = "(^|\W)um($|\W)"
    match = re.findall(um, s, re.IGNORECASE)
    if match:
        return(len(match))
    

if __name__ == "__main__":
    main()