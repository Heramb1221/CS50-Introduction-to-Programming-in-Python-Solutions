import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError!")


def convert(s):

    time = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^"+time+' to '+time+"$", s)


    if match:
        fh, fm, fx = match.group(1), match.group(2), match.group(3)
        th, tm, tx = match.group(4), match.group(5), match.group(6)
    else:
        raise ValueError("ValueError!")
    
    if fh == '12':
        if fx == 'AM':
            hour = "00"
        else:
            hour = "12"

    else:
        if fx == 'AM':
            hour = f"{int(fh):02}"
        else:
            hour = f"{int(fh)+12}"
    
    if fm == None:
        minute = "00"
    else:
        minute = f"{int(fm):02}"

    from_time = f"{hour}:{minute}"


    if th == '12':
        if tx == 'AM':
            hour = "00"
        else:
            hour = "12"

    else:
        if tx == 'AM':
            hour = f"{int(th):02}"
        else:
            hour = f"{int(th)+12}"
    
    if tm == None:
        minute = "00"
    else:
        minute = f"{int(tm):02}"

    to_time = f"{hour}:{minute}"

    return f"{from_time} to {to_time}"




if __name__ == "__main__":
    main()