#14. Build a dictionary where the keys are product names and the values are their prices.
#Implement options to:
#a. Add a new product
#b. Update price of an existing product
#c. Find products within a given price range
dict1 = {}
print("\t\t\t\t\t\tWELCOME TO MEMOSA\t\t\t\t\t ")
print("\t CHOOSE THE OPTION YOU WANT TO ACT ON")

while True:
    print("1. ADD A NEW PRODUCT")
    print("2. UPDATE A PRICE OF AN EXISTING PRODUCT")
    print("3. FIND PRODUCT WITHIN A GIVEN PRICE RANGE")
    try:
        choice = int(input("Enter the choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        product = input("Enter the name of the product: ")
        try:
            price = int(input("Enter the price of the product: "))
        except ValueError:
            print("Please enter a valid price.")
            continue
        dict1[product] = price
        print(f"Product '{product}' added/updated.")
    elif choice == 2:
        a = input("Enter the name of the product: ")
        if a in dict1:
            try:
                b = int(input(f"Enter the updated price of {a}: "))
            except ValueError:
                print("Please enter a valid price.")
                continue
            dict1[a] = b
            print(f"Price of '{a}' updated.")
        else:
            print("Product not available.")
    elif choice == 3:
        try:
            a = int(input("Enter the lowest price for product you are looking for: "))
            b = int(input("Enter the highest price for product you are looking for: "))
        except ValueError:
            print("Please enter valid numbers for price range.")
            continue
        found = False
        for product, price in dict1.items():
            if a <= price <= b:
                print(f"{product}: {price}")
                found = True
        if not found:
            print("No products found in this price range.")
    else:
        print("INVALID CHOICE")

    cont = input("DO YOU WANT TO CONTINUE (YES/NO): ").strip().lower()
    if cont != "yes":
        break