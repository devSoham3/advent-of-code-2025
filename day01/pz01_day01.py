instructions = ""

with open("dial-input.txt") as file:
    instructions = file.read()

demo_instructions = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

# instructions = demo_instructions

pointer = 50
max_q = 99
min_q = 0
ans = 0

instructions = instructions.split()
print(f"Instruction count = {len(instructions)}")

def rotate_left(pointer: int, count: int):
    global ans
    # print(f"FROM RL: {ans=}")
    
    for i in range(count):
        pointer -= 1
        if pointer == 0:
            ans += 1
        if pointer == -1:
            pointer = 99
    
    return pointer

def rotate_right(pointer: int, count: int):
    global ans
    # print(f"FROM RR: before{ans=}")

    for i in range(count):
        pointer += 1
        if pointer == 100:
            pointer = 0
            ans += 1
    
    return pointer

for i, inst in enumerate(instructions):
    # print(f"{i=}: {inst=}")
    
    dir, count = inst[0], int(inst[1:])
    
    if dir.upper() == "L":
        # print(f"-{count}")
        pointer = rotate_left(pointer, count)

    elif dir.upper() == "R":
        # print(f"+{count}")
        pointer = rotate_right(pointer, count)
    
    print(f"POINTER AT: {pointer}")

print(f"ANSWER: {ans}")