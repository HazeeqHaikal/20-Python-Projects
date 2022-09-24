from currency_converter import CurrencyConverter
from forex_python.converter import CurrencyRates

cr = CurrencyRates()
c = CurrencyConverter()

def currencyConvert():
    try:
        convertedAmount = cr.convert(currencyFrom.upper(), currencyTo.upper(), amount)
        print(f'{currencyFrom.upper()} {amount} is {currencyTo.upper()} {convertedAmount:.2f}')
    except:
        convertCurrency()

def convertCurrency():
    convertedAmount = c.convert(amount, currencyFrom.upper(), currencyTo.upper())
    # force 2 decimal places
    print(f'{currencyFrom.upper()} {amount:.2f} is {currencyTo.upper()} {convertedAmount:.2f}')
        
    
if __name__ == '__main__':
    print('Welcome to the currency converter')
    amount = float(input('Enter the amount of money to convert: '))
    currencyTo = input('Enter the currency to convert to: ')
    currencyFrom = input('Enter the currency to convert from: ')
    
    currencyConvert()
    # convertCurrency()
    
