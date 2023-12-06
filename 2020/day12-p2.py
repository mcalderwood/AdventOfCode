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
waypointOffsetX = 10
waypointOffsetY = -1
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
        waypointOffsetY -= amount
    elif action == Action.MoveSouth:
        waypointOffsetY += amount
    elif action == Action.MoveWest:
        waypointOffsetX -= amount
    elif action == Action.MoveEast:
        waypointOffsetX += amount
    elif (action == Action.TurnLeft or action == Action.TurnRight) and amount == 180:
        waypointOffsetX = -waypointOffsetX
        waypointOffsetY = -waypointOffsetY
    elif (action == Action.TurnLeft and amount == 90) or (action == Action.TurnRight and amount == 270):
        temp = waypointOffsetX
        waypointOffsetX = waypointOffsetY
        waypointOffsetY = -temp
    elif (action == Action.TurnLeft and amount == 270) or (action == Action.TurnRight and amount == 90):
        temp = waypointOffsetX
        waypointOffsetX = -waypointOffsetY
        waypointOffsetY = temp
    elif action == Action.MoveForward:
        posX += waypointOffsetX * amount
        posY += waypointOffsetY * amount
    else:
        print("Bad instruction:", instruction)

print("X: ", posX)
print("Y: ", posY)
print("Manhattan distance: ", abs(posX) + abs(posY))