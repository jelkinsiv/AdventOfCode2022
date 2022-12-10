from math import sqrt 
from numpy import sign
from enum import Enum

FILE_NAME = "Day 10/10_data.txt"

class ActionType(Enum):
    ADDX = 0
    NOOP = 1

class CRT():
    def __init__(self) -> None:
        self.sprite_position = 1
        self.sprite_length = self.sprite_position + 2
        self.image_columns_count = 40
        self.image_rows_count = 6
        self.image = [['?'] * self.image_columns_count for _ in range(self.image_rows_count)]

    @property
    def sprite_start(self):
        return self.sprite_position

    @property
    def sprite_end(self):
        return self.sprite_position + self.sprite_length

    def runCycle(self, i):
        y = i // self.image_columns_count 
        x = i % self.image_columns_count

        if (x + 1) < self.sprite_start or (x + 1) > self.sprite_end - 1:
            self.image[y][x] = '.'
        else:
            self.image[y][x] = '#'

class Action():
    def __init__(self, action: ActionType, value) -> None:
        self.action = action
        self.value: int = value

    def actionFromSting(string: str):
        action_char, *value = string.split(' ')
        if action_char == 'addx':
            return Action(ActionType.ADDX, int(value[0]))
        else:
            return Action(ActionType.NOOP, 0)

lines = [line.strip() for line in open(FILE_NAME, "r").read().split('\n')]
crt = CRT()
current_action = None
action_index = 0

for index in range(crt.image_columns_count * crt.image_rows_count):
    action_start_this_cycle = False
    if not current_action:
        line = lines[action_index % len(lines)]
        current_action = Action.actionFromSting(line)
        action_start_this_cycle = True
        action_index += 1

    crt.runCycle(index)

    if current_action.action == ActionType.NOOP or action_start_this_cycle == False:
        crt.sprite_position += current_action.value
        current_action = None        

for y in range(crt.image_rows_count):
    print(''.join([char for char in crt.image[y]]))