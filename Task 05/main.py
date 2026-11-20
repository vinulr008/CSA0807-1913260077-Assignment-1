farmer_id = input("Enter Farmer ID: ")

try:
    litres = float(input("Enter Milk Quantity: "))
    fat = float(input("Enter Fat Percentage: "))
    snf = float(input("Enter SNF Percentage: "))

    if litres < 0:
        print("Invalid Quantity")
    elif not 2.0 <= fat <= 7.0:
        print("Invalid Fat Percentage")
    elif snf < 0:
        print("Invalid SNF Percentage")
    else:
        print("\nMilk Details")
        print("Farmer ID:", farmer_id)
        print(f"Litres: {litres:8.2f}")
        print(f"Fat: {fat:8.2f}")
        print(f"SNF: {snf:8.2f}")

except ValueError:
    print("Invalid Input. Enter Numeric Values.")
