id_ranges = []
ans = 0
# Read in the input file, 1 line with comma-separated ID ranges
with open("day 2/input.txt", "r") as f:
    id_ranges = f.readline().split(",")

# Now we need to handle numbers which are repeated at least twice in a row
for id_range in id_ranges:
    start_id, end_id = map(int, id_range.split("-"))
    print(f"ID Range: {start_id} to {end_id}, Total IDs: {end_id - start_id + 1}")
    for id_num in range(start_id, end_id + 1):
        # a id is invalid if it contains a single number repated at least twice
        # ex: 99, 115115, 111, 123123, 123123123
        # it must be only that number repeated, not something like 1231234
        # cannot be invalid if the number we are checking is longer than half the ID length
        for n in range(len(str(id_num)) // 2):
            if len(str(id_num)) % (n + 1) != 0:
                continue  # cannot be made up of repeated segments of this length

            # check if the number from 0 to n is repeated at least twice in a row
            num = str(id_num)[: n + 1]
            # build repeated version
            repeated_num = num * (len(str(id_num)) // (n + 1))
            if repeated_num == str(id_num):
                print(f"  Invalid ID found: {id_num}")
                ans += id_num
                break  # no need to check further lengths

print("Sum of all invalid IDs: ", ans)
