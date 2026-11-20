BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

total = 0.0

n = int(input("Enter Number of Farmers: "))

for i in range(n):
    print("\nFarmer", i + 1)

    litres = float(input("Enter Litres: "))
    fat = float(input("Enter Fat: "))
    snf = float(input("Enter SNF: "))

    if litres < 0 or not 2.0 <= fat <= 7.0 or snf < 0:
        print("Invalid Entry")
        continue

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE

    amount = round(litres * rate, 2)
    total += amount

    print("Rate:", round(rate, 2))
    print("Payment:", amount)

print("\nTen Day Total:", round(total, 2))
