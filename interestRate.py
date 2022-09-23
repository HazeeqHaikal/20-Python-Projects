

if __name__ == "__main__":
    print("This is a monthly payment calculator.\n")
    
    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input the number of years: "))
    
    monthlyInterest = apr / 1200
    months = years * 12
    monthlyPayment = principal * monthlyInterest / (1 - 1 / (1 + monthlyInterest) ** months)
    
    print("The monthly payment is: RM", round(monthlyPayment, 2))