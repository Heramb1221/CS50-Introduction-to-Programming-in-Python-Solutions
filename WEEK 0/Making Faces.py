def convert(n):
    return n.replace(":)", "🙂").replace(":(", "🙁")

def main():
    str = input()
    c = convert(str)
    print(c)

main()