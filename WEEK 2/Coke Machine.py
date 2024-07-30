y = 50

while y > 0:
    print("Amount Due:",str(y))
    x = int(input("Insert Coin: "))

    if x == 25 or x == 10 or x == 5:
        y -=x

if y < 0:
    y = -y

print("Change Owed:",str(y))