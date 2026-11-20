BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def rate_per_litre(fat, snf):
    """Calculate the milk rate per litre."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return round(rate, 2)

def payout(litres, fat, snf):
    """Calculate the payment for milk supplied."""
    rate = rate_per_litre(fat, snf)
    return round(litres * rate, 2)

def ten_day_total(payments):
    """Calculate the total payment for ten days."""
    return round(sum(payments), 2)

payments = []

for i in range(3):
    litres = float(input("Enter Litres: "))
    fat = float(input("Enter Fat: "))
    snf = float(input("Enter SNF: "))

    amount = payout(litres, fat, snf)
    payments.append(amount)

    print("Payment:", amount)

print("Ten Day Total:", ten_day_total(payments))
