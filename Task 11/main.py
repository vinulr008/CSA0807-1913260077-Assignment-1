from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

def money(value):
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def rate_per_litre(fat, snf):
    fat_steps = int(((fat - Decimal("3.5")) * 10).to_integral_value(rounding=ROUND_HALF_UP))
    snf_steps = int(((snf - Decimal("8.5")) * 10).to_integral_value(rounding=ROUND_HALF_UP))

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return money(rate)

def payout(litres, fat, snf):
    rate = rate_per_litre(fat, snf)
    return money(litres * rate)

def ten_day_total(payments):
    return money(sum(payments, Decimal("0.00")))

payments = []

n = int(input("Enter Number of Farmers: "))

for i in range(n):
    print("\nFarmer", i + 1)

    litres = Decimal(input("Enter Litres: "))
    fat = Decimal(input("Enter Fat: "))
    snf = Decimal(input("Enter SNF: "))

    if litres < 0 or not Decimal("2.0") <= fat <= Decimal("7.0") or snf < 0:
        print("Invalid Entry")
        continue

    amount = payout(litres, fat, snf)
    payments.append(amount)

    print("Payment:", amount)

print("\nTen Day Total:", ten_day_total(payments))
