# Phone Shop Stock Tracker
# prices are fixed (hardcoded) in Rs.
phone_prices = {
    "iphone": 350000,
    "samsung": 220000,
    "xiaomi": 85000,
    "oppo": 95000,
    "nokia": 40000
}

shop_stock = {}   # phone brand -> number of phones

print("=== Phone Shop Stock Tracker ===")
print("Phones available:")
for brand in phone_prices:
    print(" ", brand.title(), "- Rs.", phone_prices[brand])

# take input from the user
while True:
    brand = input("\nEnter phone brand (or type done): ").lower().strip()

    if brand == "done":
        break

    if brand not in phone_prices:
        print("Sorry, we don't sell that brand.")
        continue

    try:
        count = int(input("How many " + brand.title() + " phones? "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if count <= 0:
        print("Number must be more than 0.")
        continue

    # if the brand was added before, add to the old count
    if brand in shop_stock:
        shop_stock[brand] = shop_stock[brand] + count
    else:
        shop_stock[brand] = count

# show the result
if len(shop_stock) == 0:
    print("\nNo phones entered.")
else:
    total_value = 0
    print("\n  Stock Summary  ")
    for brand in shop_stock:
        value = phone_prices[brand] * shop_stock[brand]
        total_value = total_value + value
        print(brand.title(), "|", shop_stock[brand], "phones | Rs.", value)

    print("     ")
    print("Total stock value: Rs.", total_value)

    # save to a text file
    file = open("phone_stock.txt", "w")
    file.write("Phone Shop Stock Report\n")
    for brand in shop_stock:
        value = phone_prices[brand] * shop_stock[brand]
        file.write(brand.title() + ": " + str(shop_stock[brand]) +
                   " phones = Rs. " + str(value) + "\n")
    file.write("Total: Rs. " + str(total_value) + "\n")
    file.close()
    print("Saved to phone_stock.txt")