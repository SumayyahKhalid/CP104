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

cakepieces = int(input("Number of pieces of cake: "))
partygoers = int(input("Number of party-goers: "))

perchild = cakepieces // partygoers
leftover = cakepieces % partygoers

print(f"Each party-goer recieves {perchild} pieces of cake")
print(f"Pieces of cakes that won't be distributes: {leftover}")
