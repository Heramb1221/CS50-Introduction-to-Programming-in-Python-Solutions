month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        if "/" in date:
            m, d, y = date.split("/")
        if "," in date:
            md , y = date.split(",")
            m,d = md.split(" ")
            m = (month.index(m)) +1

        if int(m) >12 or int(d) > 31:
            raise Exception
    except:
        pass
    else:
        break

print(f"{int(y)}-{int(m):02}-{int(d):02}")