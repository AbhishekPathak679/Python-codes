# Check if a target key exists inside a data dictionary
hardware_inventory = {"CPU": 5, "RAM": 12, "SSD": 8}
search_key = "GPU"

print("Inventory fields:", hardware_inventory)
if search_key in hardware_inventory:
    print("Status:", search_key, "is available in stock.")
else:
    print("Status:", search_key, "out of stock.")
