ranges: list[str] = []
ans = 0
with open("day 5/input.txt", "r") as f:
    for line in f:
        if line.isspace():
            break
        ranges.append(line.strip())

# sort based on lower range
ranges.sort(key=lambda x: int(x.split("-")[0]))

i: int = 0
while i < len(ranges) - 1:
    currentLower, currentUpper = ranges[i].split("-")
    nextLower, nextUpper = ranges[i + 1].split("-")
    # if there is overlap, there are 2 cases
    # case 1: nextUpper is the same or smaller, next should simply be removed
    # case 2: nextUpper is still larger, current and next should be combined
    if int(currentUpper) >= int(nextLower):
        # case 2, next range should be combined with this one
        if int(currentUpper) < int(nextUpper):
            ranges[i] = f"{currentLower}-{nextUpper}"
        # case 1 and 2 remove redundant range
        ranges.pop(i + 1)
    # only increment iof we didnt remove a range
    else:
        ans += int(currentUpper) - int(currentLower) + 1
        i += 1

lower, upper = ranges[-1].split("-")
ans += int(upper) - int(lower) + 1

print(ans)
