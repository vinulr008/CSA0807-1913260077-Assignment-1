BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

STANDARD_FAT = 3.5
STANDARD_SNF = 8.5

fat = 4.2
snf = 8.7
litres = 8.5

fat_steps = round((fat - STANDARD_FAT) / 0.1)
snf_steps = round((snf - STANDARD_SNF) / 0.1)

rate = BASE_RATE + (fat_steps * FAT_STEP_VALUE) + (snf_steps * SNF_STEP_VALUE)

amount = round(litres * rate, 2)

print("Fat Steps:", fat_steps)
print("SNF Steps:", snf_steps)
print("Rate per Litre:", round(rate, 2))
print("Total Amount:", amount)

print((4.2 - 3.5) / 0.1)
print(0.1 + 0.2)
print(2.675 * 100)

print("Using int:", int((4.2 - 3.5) / 0.1))
print("Using floor:", __import__("math").floor((4.2 - 3.5) / 0.1))
