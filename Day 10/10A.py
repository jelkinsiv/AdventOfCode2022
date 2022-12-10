from math import sqrt 
from numpy import sign
from enum import Enum

# WARNING: misread this puzzle and rather than rewrite, I'm just going to make it work

FILE_NAME = "Day 10/10_data.txt"

class ActionType(Enum):
    ADDX = 0
    NOOP = 1

class CycleQueue():
    def __init__(self) -> None:
        self.queue = []
        self.signal_strength = 1

    def addAction(self, action, cycle_id):
        cycle = self.findCycleWithId(cycle_id)
        cycle.actions.append(action)
        pass

    def processCycle(self, cycle_id):
        cycle: Cycle = self.findCycleWithId(cycle_id)
        for action in cycle.actions:
            if action.action == ActionType.ADDX:
                self.signal_strength += action.value


        signal_history.append(cycle_queue.signal_strength)
        self.queue.pop(self.queue.index(cycle))

    def findCycleWithId(self, cycle_id):
        cycle = next((cycle for cycle in cycle_queue.queue if cycle.cycle_id == cycle_id), None)
        if not cycle:
            cycle = Cycle(cycle_id)
            self.queue.append(cycle)
        return cycle


class Cycle():
    def __init__(self, cycle_id) -> None:
        self.cycle_id = cycle_id
        self.actions = []

class Action():
    def __init__(self, action: ActionType, value) -> None:
        self.action = action
        self.value: int = value

def stringToAction(string) -> Action:
    action_char, *value = string.split(' ')
    if value:
        return Action(ActionType.ADDX, int(value[0]))
    else:
        return Action(ActionType.NOOP, 0)
    
    
lines = [line.strip() for line in open(FILE_NAME, "r").read().split('\n')]
queue = []

cycle_queue = CycleQueue()

signal_history = []
running = True
run_cycles = 220
current_cycle_index = 1
cycle_queue.addAction(Action(None, 0), 0)

for index in range(run_cycles):

    input_index = (index % (len(lines)))
    action_char, *value = lines[input_index].split(' ')
    if value:
        cycle_queue.addAction(Action(None, 0), current_cycle_index)
        current_cycle_index += 1
        cycle_queue.addAction(Action(ActionType.ADDX, int(value[0])), current_cycle_index)
        current_cycle_index += 1
    else:
        cycle_queue.addAction(Action(ActionType.NOOP, 0), current_cycle_index)
        current_cycle_index += 1

    cycle_queue.processCycle(index)

for index in range(len(cycle_queue.queue)):
    cycle_queue.processCycle(index)

total_score = 0
for index in range(20, 221 ,40):
    print(signal_history[index] * index)
    total_score += (signal_history[index] * index)

print(total_score)