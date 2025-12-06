ranges: list[str] = []
ingredients: list[int] = []
ans = 0
finishedRanges = False
with open("day 5/input.txt", "r") as f:
    for line in f:
        if line.isspace():
            finishedRanges = True
            continue
        if not finishedRanges:
            ranges.append(line.strip())
        else:
            ingredients.append(int(line.strip()))

# now we need to figure out if ingredient is in any of the ranges
for ingredient in ingredients:
    for range in ranges:
        lower, upper = [int(s) for s in range.split("-")]
        # if it is found to be fresh in any range, it is fresh
        if ingredient >= lower and ingredient <= upper:
            ans += 1
            break

print(ans)
