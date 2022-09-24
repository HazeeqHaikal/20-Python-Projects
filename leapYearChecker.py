# create a function to check if a year is a leap year
# if it is a leap year, print True
# if it is not a leap year, print False

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
        
    print(f"{year} is a leap year: {leap}")


if __name__ == '__main__':
    year = int(input("Enter a year: "))
    is_leap(year)