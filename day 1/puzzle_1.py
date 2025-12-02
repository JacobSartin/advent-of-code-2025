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
    if input[0].upper() == "L":
        rotation = (rotation - rotation_amount) % dial_size
    elif input[0].upper() == "R":
        rotation = (rotation + rotation_amount) % dial_size

    if rotation == 0:
        answer += 1
    print("Current rotation position: ", rotation)

print("Total times returned to 0: ", answer)
