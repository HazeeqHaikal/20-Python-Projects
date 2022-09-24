# create a function to check if a year is a leap year
# if it is a leap year, print True
# if it is not a leap year, print False

def is_leap(year):
    
    leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    print(f"{year} is a leap year: {leap}")


if __name__ == '__main__':
    year = int(input("Enter a year: "))
    is_leap(year)