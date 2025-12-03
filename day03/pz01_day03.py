with open("battery_banks.txt") as file:
    banks = file.read()

demo_banks = """987654321111111
811111111111119
234234234234278
818181911112111"""

# banks = demo_banks

banks = banks.split()

max_jolts = []

for bank in banks:
    # print(f"{type(bank)=}")
    max_j = 0

    for i in range(len(bank) - 1):
        for j in range(i + 1, len(bank)):
            max_j = max(max_j, (10 * (int(bank[i])) + int(bank[j])))

    print(f"{max_j=}")
    max_jolts.append(max_j)

print(f"{sum(max_jolts)=}")
