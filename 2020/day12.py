from enum import Enum

with open('/Users/matt/Projects/Advent of Code/2020/aoc-day12-input.txt') as my_file:
    instructions = my_file.readlines()

class Facing(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Action(Enum):
    MoveNorth = 0
    MoveEast = 1
    MoveSouth = 2
    MoveWest = 3
    TurnLeft = 4
    TurnRight = 5
    MoveForward = 6

def ParseInstruction(str):
    amount = int(str[1:])
    if str[0] == 'N':
        return Action.MoveNorth, amount
    elif str[0] == 'E':
        return Action.MoveEast, amount
    elif str[0] == 'S':
        return Action.MoveSouth, amount
    elif str[0] == 'W':
        return Action.MoveWest, amount
    elif str[0] == 'L':
        return Action.TurnLeft, amount
    elif str[0] == 'R':
        return Action.TurnRight, amount
    elif str[0] == 'F':
        return Action.MoveForward, amount
    else:
        print("ERROR!  WTF IS ", str)

posX = 0
posY = 0
heading = 90

def NormalizeHeading():
    global heading
    while heading >= 360:
        heading -= 360
    while heading < 0:
        heading += 360

for instruction in instructions:
    action, amount = ParseInstruction(instruction.strip())

    if action == Action.MoveNorth:
        posY -= amount
    elif action == Action.MoveSouth:
        posY += amount
    elif action == Action.MoveWest:
        posX -= amount
    elif action == Action.MoveEast:
        posX += amount
    elif action == Action.TurnLeft:
        heading -= amount
        NormalizeHeading()
    elif action == Action.TurnRight:
        heading += amount
        NormalizeHeading()
    elif action == Action.MoveForward:
        if heading == 90:
            posX += amount
        elif heading == 180:
            posY += amount
        elif heading == 270:
            posX -= amount
        elif heading == 0:
            posY -= amount
        else:
            print("Invalid heading: ", heading)
    else:
        print("Bad instruction:", instruction)

print("X: ", posX)
print("Y: ", posY)
print("Manhattan distance: ", abs(posX) + abs(posY))