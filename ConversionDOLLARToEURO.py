#Issa
#10/12/22

rate = float(input("Enter the exchange rate from US to Euro: "))
currency = input("Enter the USA convert from the United States Dollar to Euro or vice versa: ")

currency = currency.lower()

if currency == "usa":
    amount = float(input("Enter the dollar amount: "))
    conversion = amount/rate
    print(amount,"dollars","is",conversion,"Euros")
    
elif currency == "euro":
    amount = float(input("Enter the Euro amount: "))
    conversion = rate*amount
    print(amount,"Euros","is",conversion,"Dollars")
    
else:
    print("Error! Please enter the correct input")
    
































