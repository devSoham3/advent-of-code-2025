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

for i, line in enumerate(reversed_problems):
    print(f"{i=}")
    print(f"{len(line)=}")
    line_items = line.split()
    print(f"{len(line_items)=}")
    print(f"{line_items[:10]=}")
    print()

    if i == 0:
        for j in line_items:
            if j == "+":
                results.append(0)
                operands.append("+")
            else:
                results.append(1)
                operands.append("*")
    else:
        for j in range(len(line_items)):
            if operands[j] == "+":
                add = int(line_items[j])
                print(f"{add=}")
                results[j] += add
            else:
                mult = int(line_items[j])
                print(f"{mult=}")
                results[j] *= mult
    print(f"{results[:20]=}")

print(f"line count = {len(problems)}")
print(f"{operands[:20]=}")
print(f"{results[:20]=}")
print(f"{sum(results)=}")