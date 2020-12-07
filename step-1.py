input_text = input()

input_list = input_text.split()

text = input_list[0]
move_count = 0
is_direction_left = True
try:
    move_count = int(input_list[1])
except:
    print("Second input is not integer.")
    exit()

if move_count < -100 or move_count >= 100:
    print("Second input is out of range.")
    exit()

direction = input_list[2].lower()
if direction != "l" and direction != "r":
    print("Third input is not l(L) or r(R).")
    exit()

if (direction == "l" and move_count > 0) or (direction == "r" and move_count < 0):
    is_direction_left = True
else:
    is_direction_left = False

result = str()
move = abs(move_count) % len(text)

if move == 0:
    result = text
    print(result)
    exit()

if is_direction_left:
    result = text[move:len(text)] + text[0:move]
else:
    result = text[-move:] + text[0:len(text)-move]

print(result)
