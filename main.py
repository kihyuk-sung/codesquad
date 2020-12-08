from rubikscube import RubiksCube
from datetime import timedelta
from time import time
from random import choice as random_choice


def parse_input(input_text):
    actions = []
    for ii in range(len(input_text)):
        letter = input_text[ii]
        letter_next = ""
        try:
            letter_next = input_text[ii+1]
        except:
            letter_next = ""
        if letter == "F" or letter == "L" or letter == "R" or letter == "U" or letter == "D" or letter == "B":
            action_tmp = letter
            if letter_next == "'":
                action_tmp = action_tmp+letter_next
            elif letter_next == "2":
                actions.append(action_tmp)
            actions.append(action_tmp)
        elif letter == "Q":
            actions.append(letter)
    return actions


start_time = time()
cube = RubiksCube()
control_count = 0
random_rotate = random_choice(range(1, 500))
while True:
    for ii in range(random_rotate):
        random_action = random_choice(["F", "B", "U", "D", "L", "R"])
        random_is_clockwise = random_choice([True, False])
        cube.rotate(random_action, random_is_clockwise)
    if not cube.check():
        break

cube.show()
print()

while True:
    print("CUBE> ", end="")
    input_text = input()

    actions = parse_input(input_text)

    for action in actions:
        if action == "Q":
            end_time = time()-start_time
            times = str(timedelta(seconds=end_time)).split(".")
            times = times[0]
            print("경과시간:", times)
            print("조작갯수:", control_count)
            print("이용해주셔서 감사합니다. 뚜뚜뚜.")
            exit()
        control_count = control_count+1
        print()
        print(action)
        face = action[0]
        is_clockwise = True
        if action.find("'") > 0:
            is_clockwise = False

        cube.rotate(face, is_clockwise)

        cube.show()
        print()

        if cube.check():
            print("조작갯수:", control_count)
            print("루빅스 큐브를 풀었습니다!")
            print("축하합니다!")
            exit()
