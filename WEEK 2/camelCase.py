str = input("camelCase: ")
s1 = str.upper()
for i in range(len(str)):
    if(str[i] == s1[i]):
        print("_"+str[i].lower(),end="")
        continue
    print(str[i],end="")
print()