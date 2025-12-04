with open("rolls.txt") as file:
    rolls = file.read()

demo_rolls = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

# rolls = demo_rolls

rolls = rolls.split()
rolls = [list(roll) for roll in rolls]
# 139 rows, 139 cols
# for roll in rolls:
#     print(roll)

acc_rolls = 0

def remove_rolls(rolls, acc_rolls):

    cols = len(rolls[0])
    rows = len(rolls)
    acc_ind = []

    for x in range(rows):
        for y in range(cols):
            if rolls[x][y] != "@":
                continue
            adj_rolls = 0
            # adj_coords = l, tl, t, tr, r, br, b, bl
            adj_coords = ((x-1), y), ((x-1), (y-1)), (x, (y-1)), ((x+1), (y-1)), ((x+1), y), ((x+1), (y+1)), (x, (y+1)), ((x-1), (y+1))

            for coord in adj_coords:
                if coord[0] < 0 or coord[0] >= rows or coord[1] < 0 or coord[1] >= cols:
                    continue
                if rolls[coord[0]][coord[1]] == '@':
                    adj_rolls += 1
            
            # print(f"{adj_rolls}")
            if adj_rolls < 4:
                acc_rolls += 1
                # print(f"{rolls[x][y]=}")
                acc_ind.append((x, y))

    for ind in acc_ind:
        rolls[ind[0]][ind[1]] = "x"

    return rolls, acc_rolls, len(acc_ind)

rolls, acc_rolls, removed = remove_rolls(rolls, acc_rolls)

while removed > 0:
    rolls, acc_rolls, removed = remove_rolls(rolls, acc_rolls)
    # print(f"{acc_rolls=}")

print(f"{acc_rolls=}")