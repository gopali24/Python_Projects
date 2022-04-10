from forex_python.converter import CurrencyRates

c=CurrencyRates()
amt = int(input("Enter the amount: "))
cur1 = input("From currency: ").upper()
cur2 = input("To currency: ").upper()
print(cur1," To ",cur2)
res = c.convert(cur1,cur2,amt)
print("%.2f"%res)