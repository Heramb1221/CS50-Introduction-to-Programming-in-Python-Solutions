str = input("Greeting: ").casefold().strip()
if str.startswith('h'):
    if str.startswith('hello'):
        print("$0")
    else:
        print("$20")
else:
    print("$100")