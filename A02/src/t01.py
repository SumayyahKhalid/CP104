"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = "2022-10-10"
-------------------------------------------------------
"""

TAXRATE = 18.5
sales = float(input("Enter the total sales: $ "))
TaxToPay = (sales * TAXRATE) / 100

print("\n\nProjected Tax Report")
print("------------------------------")
print(f"Total sales: ${sales:.2f}")
print(f"Annual tax: %{TAXRATE:.2f}")
print("------------------------------")
print(f"Tax: ${TaxToPay:.2f}")
