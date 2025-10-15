while True:
    name = input("Enter customer's name: ")
    total = 0

    while True:
        print("Enter the amount & quantity of itmes: ")
        amount = float(input("Enter the amount: "))
        quantity = float(input("Enter the quantity: "))
        total = total +  (amount * quantity)

        repeat = input("Do you wish to continue adding more items? (Y/N): ")
        if repeat == "N" or repeat == "n":
            break

    print ("-"*40)
    print("Name: ", name)
    print("Amount to be paid: ", total)
    print("************ Happy Shopping!! ************")

    repeat1 = input("Do you wish to continue? (Y/N): ")
    if repeat1 == "N" or repeat1 == "n":
        break