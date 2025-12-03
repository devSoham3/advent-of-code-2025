with open("battery_banks.txt") as file:
    banks = file.read()

demo_banks = """987654321111111
811111111111119
234234234234278
818181911112111"""

# banks = demo_banks

banks = banks.split()

max_jolts = []

def find_max(ind_min, ind_max, num):
    max_n, i_n = 0, -1

    for i in range(ind_min, ind_max):
        if int(num[i]) > max_n:
            max_n, i_n = int(num[i]), i
    
    return max_n, i_n

for bank in banks:
    max_j = 0
    i_prev = -1

    for i in range(12):
        max_n, i_n = find_max(i_prev + 1, (len(bank) - (12 - (i + 1))), bank)
        i_prev = i_n
        max_j += max_n * 10**(12 - (i + 1))
    
    max_jolts.append(max_j)

print(f"{sum(max_jolts)=}")
