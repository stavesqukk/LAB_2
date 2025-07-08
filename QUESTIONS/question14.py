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
    choice = int(input("Enter the choice: "))

    if choice == 1:
        product = input("Enter the name of the product: ")
        price = int(input("Enter the price of the product: "))
        dict1[product] = price
        print(f"Product '{product}' added/updated.")
    elif choice == 2:
        a = input("Enter the name of the product: ")
        if a in dict1:
            b = int(input(f"Enter the updated price of {a}: "))
            dict1[a] = b
            print(f"Price of '{a}' updated.")
        else:
            print("Product not available.")
    elif choice == 3:
        a = int(input("Enter the lowest price for product you are looking for: "))
        b = int(input("Enter the highest price for product you are looking for: "))
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