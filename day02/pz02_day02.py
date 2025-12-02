demo_ids = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528, \
446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

ids = ""
invalids = []

with open("ids.txt") as file:
    ids = file.read()

# ids = demo_ids

ids = ids.split(",")

print(f"{ids=}")

def check_id(id: int) -> bool:
    id = str(id)
    n = len(id)
    
    for unit in range(1, n):
        elms = set()
        
        if (n % unit) == 0:
            # print(f"\ndividing {id} into parts of size {unit} to have total {n/unit} parts")
            # print("parts:", end=" ")
            
            for i in range(0, n, unit):
                # print(f"{id[i:i + unit]}", end=", ")
                elms.add(id[i:i + unit])
            # print()
    
        if len(elms) == 1:
            return True
    
    return False

for rng in ids:
    start, end = rng.split("-")
    start, end = int(start), (int(end) + 1)
    # print(f"\n{start=}, {end=}")

    for id in range(start, end):
        # print(id, end=", ")
        if check_id(id):
            invalids.append(id)

print(f"{invalids=}")
print(f"{sum(invalids)=}")