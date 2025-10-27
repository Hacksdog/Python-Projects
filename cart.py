# 3. SHOPPING CART SYSTEM
# --------------------------------------------------
# Concepts: Lists, Dictionaries, Loops
# Description:
# - Display a list of items with prices.
# - Let the user add/remove items from a cart.
# - Calculate the total bill and apply discounts.


items = [
    ["Apple", 50],
    ["Banana", 20],
    ["Milk", 40],
    ["Bread", 30],
    ["Eggs", 60]
]

print("Item\t\tPrice (₹)")
print("-" * 20)
for item, price in items:
    print(f"{item}\t\t{price}")


def price():
    cart_price = 0
    while True:
        pick_item = input("Enter which item you want to add in your cart?\n").title()
        found = False

        for item_name, item_price in items:
            if pick_item == item_name:
                cart_price += item_price
                found = True
                print(f"{item_name} added to cart.")
                break

        if not found:
            print("Item not found. Please try again.")

        pick_item2 = input("Want to add any other item? 'y' for yes, 'n' for no: ").lower()
        if pick_item2 != 'y':
            break

    return cart_price


f_cart_price = price()
dis = f_cart_price * 0.1
dis1 = f_cart_price - dis
print(f"\nYour Total Price Is: ₹{f_cart_price}")
print(f"Price after 10% discount: ₹{dis1}")



    




