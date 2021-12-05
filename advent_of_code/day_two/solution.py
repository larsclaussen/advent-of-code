from dataclasses import dataclass
from typing import Union
import operator
from pathlib import Path


@dataclass
class BaseTarget:
    value: int

    def __mul__(self, other):
        return self.value * other.value


class Horizontal(BaseTarget):
    ...


class Depth(BaseTarget):
    ...


class Aim(BaseTarget):
    ...



@dataclass
class Map:
    target_operator: Union[operator.add, operator.sub, operator.mul]
    target: Union[Horizontal, Depth, Aim]


@dataclass
class ExtMap:
    target_operator: operator.mul
    target: Depth
    mul_by: Aim


horizontal = Horizontal(0)
depth = Depth(0)
aim = Aim(0)

def part_two():
    commands = {
        "down": Map(target_operator=operator.add, target=aim),
        "up": Map(target_operator=operator.sub, target=aim),
        "forward": [
            Map(target_operator=operator.add, target=horizontal), 
            ExtMap(target_operator=operator.mul, target=depth, mul_by=aim),
        ], 
    }
    input_file = Path("./data/input.txt")
    with input_file.open("r") as f:
        for line in f:
            cmd, value = line.strip("\n").split(" ")
            m = commands[cmd]
            if cmd != "forward":
                result = m.target_operator(m.target.value, int(value))
                m.target.value = result
                continue
            forw = m[0]
            result = forw.target_operator(forw.target.value, int(value))
            forw.target.value = result
            dep = m[1]
            result = dep.target_operator(dep.mul_by.value, int(value))
            dep.target.value += result

    print(horizontal)
    print(depth)
    print(aim)
    answer = horizontal * depth
    print(f"ANSWER: {answer}")


def part_one():

    commands = {
        "forward": Map(target_operator=operator.add, target=horizontal), 
        "down": Map(target_operator=operator.add, target=depth),
        "up": Map(target_operator=operator.sub, target=depth)
    }

    input_file = Path("./data/input.txt")
    with input_file.open("r") as f:
        for line in f:
            cmd, cnt = line.strip("\n").split(" ")
            m = commands[cmd]
            result = m.target_operator(m.target.value, int(cnt))
            m.target.value = result

    print(horizontal)
    print(depth)
    answer = horizontal * depth
    print(f"ANSWER: {answer}")

if __name__ == "__main__":
    # part_one()
    part_two()
