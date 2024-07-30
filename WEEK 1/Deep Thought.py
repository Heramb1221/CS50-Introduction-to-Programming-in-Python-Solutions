str = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").casefold().strip()

if str == '42' or str == 'forty two' or str == 'forty-two':
    print("yes")
else:
    print("no")