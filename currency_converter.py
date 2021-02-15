from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

def fiatMoney():
    c = CurrencyRates()

    amount = int(input("enter the amount: \n"))
    from_currency = input("From currency: \n").upper()
    to_currency = input("To Currency: \n").upper()

    print(from_currency, " To ", to_currency, amount)

    result = c.convert(from_currency, to_currency, amount)

    print(result)

def cryptoMoney():
    b = BtcConverter()

    amount = int(input("enter the amount: \n"))
    from_currency = input("From currency: \n").upper()
    to_currency = input("To Currency: \n").upper()
    print(from_currency, " To ", to_currency)

    result = b.convert_btc_to_cur(amount, to_currency )

    print(result)

# Menu Choice
print("------- Menu -------")
print(" Choose one Option:\n")

choose = int (input(" [1] Fiat Money \n [2] CryptoCurrency\n"))

if choose == 1:
    fiatMoney()
elif choose == 2:
    cryptoMoney()
