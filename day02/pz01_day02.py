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
    # print(f"\n{id=}, {n=}")
    p1, p2 = id[:int(n/2)], id[int(n/2):]

    # print(f"{p1=}, {p2=}")
    if p1 == p2:
        return True
    return False

for rng in ids:
    start, end = rng.split("-")
    start, end = int(start), (int(end) + 1)
    # print(f"\n{start=}, {end=}")

    for id in range(start, end):
        # print(id, end=", ")
        
        if len(str(id)) % 2 == 0:
            if check_id(id):
                invalids.append(id)
        else:
            continue

print(f"{invalids=}")
print(f"{sum(invalids)=}")