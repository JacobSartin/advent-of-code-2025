banks: list[str] = []
ans = 0
# number fo batteries in a bank that can be used
ACTIVE_BATTERIES = 2
# Read in the input file, 1 bank per line
with open("day 3/input.txt", "r") as f:
    for line in f:
        banks.append(line.strip())

# main assumption: we can greedily search for the largest number for the furthest left digit
# this will always result in the largest number, repeat for each following digit

for index, bank in enumerate(banks):
    # find max digit, index of max
    max: list[int] = [0] * (ACTIVE_BATTERIES + 2)
    joltage: str = ""

    for i in range(1, ACTIVE_BATTERIES + 1):
        # need to have batteries remaining for the following active slots
        for j in range(max[i - 1] + 1, len(bank) - (ACTIVE_BATTERIES - i)):
            if int(bank[j]) > int(bank[max[i]]):
                max[i] = j
                # 9 is max value, dont need to continue
                if int(bank[j]) == 9:
                    break
        joltage += bank[max[i]]
        max[i + 1] = max[i] + 1
    ans += int(joltage)
    print(f"Max joltage for bank {index} is {joltage}")
print(f" ans: {ans}")
