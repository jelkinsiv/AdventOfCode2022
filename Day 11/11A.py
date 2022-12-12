from enum import Enum
from math import prod

FILE_NAME = "Day 11/11_data.txt"

class Operators(Enum):
    ADD = 0
    SUB = 1
    MULTIPLE = 2
    DIVIDE = 3
class Monkey():
    def __init__(self, raw_monkey_data) -> None:
        self.monkey_id = 0
        self.items = []
        self.inspect_operator: Operators = None
        self.inspect_value = 0
        self.test_value = 0
        self.test_target_true = 0
        self.test_target_false = 0
        self.items_inspected = 0

        self.hydrateFromString(raw_monkey_data)

    def inspect(self):
        self.items_inspected += 1

        item = self.items[0]
        op_number = item if self.inspect_value == 'old' else int(self.inspect_value)
        match self.inspect_operator:
            case Operators.ADD:
                item += op_number
            case Operators.SUB:
                item -= op_number
            case Operators.MULTIPLE:
                item *= op_number
            case Operators.DIVIDE:
                item //= op_number

        self.items[0] = item

    def throw(self, game):
        item = self.items[0]
        if item % self.test_value == 0:
            target_monkey = game.monkeyById(self.test_target_true) 
        else:
            target_monkey = game.monkeyById(self.test_target_false)
        target_monkey.items.append(item)
        self.items.pop(0)
        pass

    def hydrateFromString(self, raw_monkey_data):
        lines = raw_monkey_data.split("\n")
        
        self.monkey_id = int(lines[0][-2])

        _, items_string = lines[1].split(": ")
        self.items = [int(item) for item in items_string.split(",")]

        operation = lines[2].split(" = ")[1].split(" ")
        self.inspect_operator = Operators("+-*/".index(operation[1]))
        self.inspect_value = operation[2]

        self.test_value = int(lines[3].split(" by ")[1].strip())
        self.test_target_true = int(lines[4][-1])
        self.test_target_false = int(lines[5][-1])

class MonkeyGame():
    def __init__(self, monkeys, round_count) -> None:
        self.monkeys = monkeys
        self.round_count = round_count
        self.mod_value = prod([monkey.test_value for monkey in self.monkeys])

    def run_game(self):
        for i in range(self.round_count):
            self.start_round()

    def start_round(self):
        for monkey in self.monkeys:
            for _ in range(len(monkey.items)):
                monkey.inspect()
                monkey.items[0] = self.manage_worry(monkey.items[0])
                monkey.throw(self)
    
    def manage_worry(self, item) -> int:

        # part A
        #return item //= 3

        return item % self.mod_value

    @property
    def monkey_business_score(self):
        return prod(sorted([monkey.items_inspected for monkey in self.monkeys])[-2:])

    def monkeyById(self, monkey_id):
        return [monkey for monkey in self.monkeys if monkey.monkey_id == monkey_id][0]

raw_monkey_data = [data.strip() for data in open(FILE_NAME, "r").read().split('\n\n')]
game = MonkeyGame([Monkey(monkey_raw) for monkey_raw in raw_monkey_data], 10000)
game.run_game()

print(f"Monkey Business: {game.monkey_business_score}")