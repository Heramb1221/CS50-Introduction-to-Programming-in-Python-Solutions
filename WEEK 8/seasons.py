from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    date1 = get_date()
    today = date.today()

    time = get_time(today, date1)

    minutes = p.number_to_words(time, andword="")

    print(minutes.capitalize() + " minutes")


def get_date():
    try:
        inpt = input("Date of Birth: ")
        return date.fromisoformat(inpt)
    except ValueError:
        sys.exit("Invalid date")

def get_time(t,d):
    dif = t-d
    min = round((dif.total_seconds()/ 60))
    return min



if __name__ == "__main__":
    main()
