'''
Created on 29 Oct 2026

@author: ymang
'''
price = float(input("Enter the price of the sale item (e.g., 3.99 or 5.00): "))
state = input("Enter the state to which the item to be shipped (e.g., TX, LA, CA): ").strip().upper()
if state == "TX" or state == "LA":
    shipping_tax = 1.25
elif state == "CA":
    shipping_tax = 3.25
else:
    shipping_tax = 0.50
print(f"The shipping tax is: {shipping_tax}")