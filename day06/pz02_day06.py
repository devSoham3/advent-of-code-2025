with open("problems.txt") as file:
    problems = file.read()

demo_problems = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

# problems = demo_problems

problems = problems.split("\n")
reversed_problems = list(reversed(problems))

results = []
operands = []
max_num = 0
f_probs = []

for i, line in enumerate(problems[:-1]):
    print(f"{i=}")
    print(f"{len(line)=}")
    line_items = line.split()
    print(f"{len(line_items)=}")
    print(f"{line_items[:10]=}")
    print()
    for j in range(len(line_items)):
        if len(line_items[j]) < 4:
            line_items[j] = (4-len(line_items[j]))*'0' + line_items[j]
    f_probs.append(line_items)

print(f"{max_num=}")
print()
for l in f_probs:
    print(l[:20])

for 

print(f"line count = {len(problems)}")
print(f"{operands[:20]=}")
print(f"{results[:20]=}")
