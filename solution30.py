# Simulating a simple wallet balance deduction check
wallet_balance = 1000
purchase_amount = 350

print("Current Wallet Balance: Rs.", wallet_balance)
print("Attempting to purchase item for: Rs.", purchase_amount)

if wallet_balance >= purchase_amount:
    wallet_balance = wallet_balance - purchase_amount
    print("Status: Purchase Successful!")
    print("Remaining Balance: Rs.", wallet_balance)
else:
    print("Status: Insufficient funds in wallet.")
