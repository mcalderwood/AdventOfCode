from pathlib import Path

def step():
    global xPos, yPos, xVel, yVel
    xPos += xVel
    yPos += yVel
    if xVel > 0:
        xVel -= 1
    elif xVel < 0:
        xVel += 1
    yVel -= 1

path = Path(__file__).parent / "aoc-day16-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

targetXMin = 32
targetXMax = 65
targetYMin = -225
targetYMax = -177
xVelMin = 8
xVelMax = 66
yVelMin = -225
yVelMax = 500

#targetXMin = 20
#targetXMax = 30
#targetYMin = -10
#targetYMax = -5
#
#xVelMin = 6
#xVelMax = 31
#yVelMin = -10
#yVelMax = 200

maxY = targetYMin
count = 0
for xV in range(xVelMin,xVelMax):
    for yV in range(yVelMin,yVelMax):
        xPos = 0
        yPos = 0
        xVel = xV
        yVel = yV
        maxY_this_time = targetYMin

        while yPos > targetYMin:
            step()
            if yPos > maxY_this_time:
                maxY_this_time = yPos
            if xPos >= targetXMin and xPos <= targetXMax and yPos >= targetYMin and yPos <= targetYMax:
                print("HIT! using initial X Velocity ", xV, " and Y Velocity ", yV)
                count += 1
                break
                if maxY_this_time > maxY:
                    maxY = maxY_this_time
                    #print("New high score! ", maxY)

print (count)
#print (maxY)