from decimal import Decimal
import time

def calculate_float(n):
    total = 0.0

    for i in range(n):
        total += 33.40

    return total

def calculate_decimal(n):
    total = Decimal("0.00")

    for i in range(n):
        total += Decimal("33.40")

    return total

sizes = [300, 6000, 150000]

for n in sizes:
    start = time.perf_counter()
    float_total = calculate_float(n)
    float_time = time.perf_counter() - start

    start = time.perf_counter()
    decimal_total = calculate_decimal(n)
    decimal_time = time.perf_counter() - start

    print("\nNumber of Payments:", n)
    print("Float Total:", float_total)
    print("Decimal Total:", decimal_total)
    print("Difference:", Decimal(str(float_total)) - decimal_total)
    print("Float Time:", float_time)
    print("Decimal Time:", decimal_time)

rate_cache = {}

def cached_rate(fat, snf):
    key = (fat, snf)

    if key not in rate_cache:
        fat_steps = round((fat - 3.5) / 0.1)
        snf_steps = round((snf - 8.5) / 0.1)

        rate_cache[key] = round(
            30 + fat_steps * 0.40 + snf_steps * 0.30, 2
        )

    return rate_cache[key]

print("\nCached Rate:", cached_rate(4.2, 8.7))
print("Rate Table:", rate_cache)
