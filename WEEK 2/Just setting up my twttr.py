v = ['a','e','i','o','u','A','E','I','O','U']

str = input("Input: ")

for letters in str:
    if letters in v:
        pass
    else:
        print(letters,end='')
print()