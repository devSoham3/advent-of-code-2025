with open("tiles.txt") as file:
    tiles = file.read()

demo_tiles = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

tiles = demo_tiles

tiles = [[int(t.split(",")[0]), int(t.split(",")[1])] for t in tiles.split()]

print(f"{len(tiles)=}")
print(f"{tiles[:10]}")

def calculate_area(p1, p2):
    area = abs((p1[0] - p2[0]) + 1) * abs((p1[1] - p2[1]) + 1)
    return area

max_area = 0
green_tiles = []

t = 0
n = len(tiles)

print(f"{green_tiles=}")
print()

for i in range(len(tiles)):
    for j in range(i, len(tiles)):
        print(f"Calculating for {tiles[i]}, {tiles}")
        diag = []
        p1, p2 = tiles[i], (tiles[j][0]+1, tiles[j][1]+1)
        print(f"{p1=}, {p2=}")
        while p2 != p1:
            diag.append(p2)
            p2 = p2[0] + 1, p2[1] + 1
        
        max_area = max(max_area, calculate_area(tiles[i], tiles[j]))

print(f"{max_area=}")