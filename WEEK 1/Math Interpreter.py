str = input("Expression: ")
x, y, z = str.split(" ")

match y:
    case '+':
        print(float(x)+float(z))
    case '-':
        print(float(x)-float(z))
    case '*':
        print(float(x)*float(z))
    case '/':
        print(float(x)/float(z))