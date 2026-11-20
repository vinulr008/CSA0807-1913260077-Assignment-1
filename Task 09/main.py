BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def rate_per_litre(fat, snf):
    if not 2.0 <= fat <= 7.0:
        raise ValueError("Fat must be between 2.0 and 7.0")

    if not 0 <= snf <= 12.0:
        raise ValueError("Invalid SNF")

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    return round(BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE, 2)

def payout(litres, fat, snf):
    if litres < 0:
        raise ValueError("Litres cannot be negative")

    return round(litres * rate_per_litre(fat, snf), 2)

def ten_day_total(payments):
    return round(sum(payments), 2)

def test_calculator():
    assert rate_per_litre(3.5, 8.5) == 30.00
    assert rate_per_litre(4.2, 8.7) == 33.40
    assert rate_per_litre(3.1, 8.3) == 27.80
    assert payout(10, 3.5, 8.5) == 300.00
    assert payout(8.5, 4.2, 8.7) == 283.90

    try:
        payout(-5, 3.5, 8.5)
        assert False
    except ValueError:
        pass

    try:
        rate_per_litre(8.0, 8.5)
        assert False
    except ValueError:
        pass

    print("All Tests Passed Successfully")

test_calculator()

payments = []

for i in range(5):
    print("\nFarmer", i + 1)

    try:
        litres = float(input("Enter Litres: "))
        fat = float(input("Enter Fat: "))
        snf = float(input("Enter SNF: "))

        amount = payout(litres, fat, snf)
        payments.append(amount)

        print("Payment:", amount)

    except ValueError as error:
        print("Error:", error)

print("Total Payment:", ten_day_total(payments))
