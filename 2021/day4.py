import sys
import re
from pathlib import Path

class BingoBoard:
    
    def __init__(self):
        self.board = [ [0] * 5 for i in range(5)]
        self.marks = [ [False] * 5 for i in range(5)]

    def draw(self, draw_num):
        for y in range(5):
            for x in range(5):
                if self.board[x][y] == draw_num:
                    self.marks[x][y] = True
                    return self.checkForWin()
        return False
    
    def checkForWin(self):
        for y in range(5):
            num_true = 0
            for x in range(5):
                if self.marks[x][y] == True:
                    num_true += 1
            if num_true == 5:
                return True
        
        for x in range(5):
            num_true = 0
            for y in range(5):
                if self.marks[x][y] == True:
                    num_true += 1
            if num_true == 5:
                return True

        return False

    def score(self, winning_draw):
        unmarked_sum = 0
        for y in range(5):
            for x in range(5):
                if self.marks[x][y] == False:
                    unmarked_sum += self.board[x][y]
        return unmarked_sum * winning_draw


path = Path(__file__).parent / "aoc-day4-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

# Create array of 5x5 boards
bingo_boards = []
draw_numbers = input_array[0].split(",")

for i in range(2,len(input_array),6):
    new_board = BingoBoard()

    for j in range(5):
        m = re.match(r"\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)", input_array[i+j])

        for k in range(5):
            new_board.board[j][k] = int(m.group(k+1))
    
    bingo_boards.append(new_board)
    
for draw in draw_numbers:
    for board in bingo_boards:
        if board.draw(int(draw)) == True:
            print (board.score(int(draw)))
            exit(0)
