dial_size = 100
rotation = 50
finished = False
answer = 0
inputs = []
with open("day 1/input.txt", "r") as f:
    for line in f:
        inputs.append(line.strip())

for input in inputs:
    rotation_amount = int(input[1:])
    print(
        "Rotation amount: ",
        rotation_amount if input[0].upper() == "R" else -rotation_amount,
    )

    # count how many complete rotations (zero crossings)
    passed_zero = rotation_amount // dial_size
    rotation_amount = rotation_amount % dial_size

    # apply the rotation and check if we cross 0 on the partial amount
    old_rotation = rotation
    if input[0].upper() == "L":
        rotation = rotation - rotation_amount
        # check if we crossed 0 going left (from positive to negative)
        if rotation <= 0 and old_rotation > 0:
            passed_zero += 1
    else:
        rotation = rotation + rotation_amount
        # check if we crossed 0 going right (crossing dial_size)
        if rotation >= dial_size and old_rotation < dial_size:
            passed_zero += 1

    # normalize to 0-99 range
    rotation = rotation % dial_size

    print("Current rotation position: ", rotation)
    print("Times passed 0 this move: ", passed_zero)
    answer += passed_zero
    print()

print("Total times clicked at or by 0: ", answer)
