with open("ingredients.txt") as file:
    ing = file.read()

demo_ing = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

# ing = demo_ing

ing_lists, ing = [[int(i.split("-")[0]), int(i.split("-")[1])] for i in (ing.split("\n\n")[0].strip()).split()], [int(i) for i in (ing.split("\n\n")[1].strip()).split()]
# print(f"{ing_lists=}")
# print()
# print(f"{ing=}")
print(f"{len(ing_lists)=}")
print()
print(f"{len(ing)=}")

ing_lists = sorted(ing_lists, key=lambda x: x[0])
ing = sorted(ing)

# print(f"sorted {ing_lists=}")
# print()
print(f"sorted {ing=}")

merged_ing_list = []

for s, e in ing_lists:
    if merged_ing_list and merged_ing_list[-1][1] >= s:
        merged_ing_list[-1][1] = max(merged_ing_list[-1][1], e)
    else:
        merged_ing_list.append([s, e])

print(f"{merged_ing_list=}")
print(f"{len(merged_ing_list)=}")

fresh_set = set()
spoiled = set()

def binary_search_ing(ing_id, intervals):
    l, r = 0, (len(intervals) - 1)

    while l <= r:
        m = (l + r) // 2

        if ing_id >= intervals[m][0] and ing_id <= intervals[m][1]:
            return True
        
        elif ing_id < intervals[m][0]:
            r = m - 1
        else:
            l = m + 1

    return False

for i in ing:
    if binary_search_ing(i, merged_ing_list):
        fresh_set.add(i)
    else:
        spoiled.add(i)

print(f"{fresh_set=}")
print(f"{len(fresh_set)=}")
print(f"{len(spoiled)=}")
print(f"{len(ing)=} \n{(len(fresh_set) + len(spoiled))=}")
