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

flength = float(input("Foundation length (m): "))
fwidth = float(input("Foundation width (m): "))
fheight = float(input("Foundation height (m): "))
wheight = float(input("Wall height (m): "))
cofconcrete = float(input("Cost of concrete ($/m^3): "))
cofbricks = float(input("Cost of bricks ($/m^2): "))

volumeFoundation = flength * fwidth * fheight
totalcofconcrete = cofconcrete * volumeFoundation
wallArea = 2 * (wheight * fwidth + wheight * flength)
totalcostbricks = wallArea * cofbricks
totalcost = totalcofconcrete + totalcostbricks

print(f"Concrete needed for foundation (m^3): {volumeFoundation:.2f}")
print(f"Cost of concrete: {totalcofconcrete:,.2f}")
print(f"Bricks needed for walls (m^2): {wallArea:.2f}")
print(f"Cost of bricks: {totalcostbricks:,.2f}")
print(f"Total cost: {totalcost:,.2f}")
