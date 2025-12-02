id_ranges = []
ans = 0
# Read in the input file, 1 line with comma-separated ID ranges
with open("day 2/input.txt", "r") as f:
    id_ranges = f.readline().split(",")

for id_range in id_ranges:
    start_id, end_id = map(int, id_range.split("-"))
    print(f"ID Range: {start_id} to {end_id}, Total IDs: {end_id - start_id + 1}")
    for id_num in range(start_id, end_id + 1):
        # a id is invalid if it contains a single number repated twice
        # ex: 99, 115115
        if len(str(id_num)) % 2 != 0:
            continue  # odd length IDs cannot be invalid
        first_half = str(id_num)[: len(str(id_num)) // 2]
        second_half = str(id_num)[len(str(id_num)) // 2 :]
        if first_half == second_half:
            print(f"  Invalid ID found: {id_num}")
            ans += id_num

print("Sum of all invalid IDs: ", ans)
