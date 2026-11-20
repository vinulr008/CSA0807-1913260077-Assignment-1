from decimal import Decimal, ROUND_HALF_UP

STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")

def money(value):
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def calculate_steps(value, standard):
    difference = (value - standard) * 10
    return int(difference.to_integral_value(rounding=ROUND_HALF_UP))

def get_rate_card(month):
    if 4 <= month <= 6:
        return Decimal("32.00"), Decimal("0.45"), Decimal("0.30")
    else:
        return Decimal("30.00"), Decimal("0.40"), Decimal("0.30")

def rate_per_litre(fat, snf, month):
    base_rate, fat_value, snf_value = get_rate_card(month)

    fat_steps = calculate_steps(fat, STANDARD_FAT)
    snf_steps = calculate_steps(snf, STANDARD_SNF)

    rate = base_rate + (fat_steps * fat_value) + (snf_steps * snf_value)

    return money(rate)

def calculate_bonus(total_litres):
    if total_litres > Decimal("500"):
        return Decimal("0.50")
    return Decimal("0.00")

def calculate_payment(litres, fat, snf, month):
    rate = rate_per_litre(fat, snf, month)
    return money(litres * rate)

def ten_day_payment(entries, month):
    total_litres = sum(
        (entry[0] for entry in entries),
        Decimal("0.00")
    )

    bonus = calculate_bonus(total_litres)
    total_payment = Decimal("0.00")

    for litres, fat, snf in entries:
        rate = rate_per_litre(fat, snf, month)
        amount = money(litres * (rate + bonus))
        total_payment += amount

    return money(total_payment), total_litres, bonus

entries = []

n = int(input("Enter Number of Farmers: "))
month = int(input("Enter Month (1-12): "))

if not 1 <= month <= 12:
    print("Invalid Month")
else:
    for i in range(n):
        print("\nFarmer", i + 1)

        try:
            litres = Decimal(input("Enter Litres: "))
            fat = Decimal(input("Enter Fat Percentage: "))
            snf = Decimal(input("Enter SNF Percentage: "))

            if litres < 0:
                print("Invalid Quantity")
                continue

            if not Decimal("2.0") <= fat <= Decimal("7.0"):
                print("Invalid Fat Percentage")
                continue

            if snf < 0:
                print("Invalid SNF Percentage")
                continue

            entries.append((litres, fat, snf))

            rate = rate_per_litre(fat, snf, month)
            print("Rate per Litre:", rate)
            print("Payment:", money(litres * rate))

        except Exception:
            print("Invalid Input")

    if entries:
        total, litres, bonus = ten_day_payment(entries, month)

        print("\n----- TEN DAY PAYMENT SUMMARY -----")
        print("Month:", month)
        print("Total Litres:", litres)
        print("Bonus Per Litre:", bonus)
        print("Total Payment:", total)
