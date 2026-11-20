from decimal import Decimal

payments = ["33.40"] * 1000 + ["0.10"] * 3

def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total

def total_decimal(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)
    return total

print(type(10))
print(type(10.0))
print(type("10"))
print(type(True))
print(type([10, 8.5]))

print(7 / 2)
print(7 // 2)
print(7 % 2)
print(-7 // 2)

print(0.1 + 0.2 == 0.3)

print("float :", total_float(payments))
print("Decimal:", total_decimal(payments))

print(0.1 + 0.2 == 0.3, Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

wrong_total = sum(Decimal(float(x)) for x in payments)
print("Wrong Decimal:", wrong_total)
