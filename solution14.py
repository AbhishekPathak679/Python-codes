# Calculate the total cost of items purchased from a store catalog
price_list = {"notebook": 40, "pen": 10, "eraser": 5, "bag": 300}

# Items added to the cart
notebooks_bought = 3
pens_bought = 5

total_bill = (price_list["notebook"] * notebooks_bought) + (price_list["pen"] * pens_bought)

print("Shopping summary:")
print("Notebooks bought:", notebooks_bought)
print("Pens bought:", pens_bought)
print("Grand Total Bill Amount: Rs.", total_bill)

