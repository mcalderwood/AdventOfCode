from enum import Enum

with open('/Users/matt/Projects/Advent of Code/2020/aoc-day11-input.txt') as my_file:
    seat_rows = my_file.readlines()

class SeatState(Enum):
    FLOOR = 0
    EMPTY = 1
    OCCUPIED = 2

seats = []

def FindNextSeat(startRow, startCol, rowDirection, colDirection):
    global seats

    row = startRow + rowDirection
    col = startCol + colDirection

    while row >= 0 and row < len(seats) and col >= 0 and col < len(seats[row]):
        if seats[row][col] != SeatState.FLOOR:
            return seats[row][col]
        else:
            row += rowDirection
            col += colDirection
    
    return SeatState.EMPTY

def NumberOfAdjacentOccupiedSeats(row, col):
    global seats
    count = 0

    for rowDirection in [-1, 0, 1]:
        for colDirection in [-1, 0, 1]:

            # Skip the seat itself
            if rowDirection == 0 and colDirection == 0:
                continue

            if FindNextSeat(row, col, rowDirection, colDirection) == SeatState.OCCUPIED:
                count += 1
    
    return count

def ShowSeats():
    global seats
    for row in seats:
        for seat in row:
            if seat == SeatState.OCCUPIED:
                print('#',end='')
            elif seat == SeatState.EMPTY:
                print('L',end='')
            elif seat == SeatState.FLOOR:
                print('.',end='')
            else:
                print("WTF")
        print()
    print()


for seat_row in seat_rows:
    row = []
    for seat in seat_row.strip():
        if seat == ".":
            row.append(SeatState.FLOOR)
        elif seat == "L":
            row.append(SeatState.EMPTY)
        elif seat == "#`":
            row.append(SeatState.OCCUPIED)
        else:
            print("WTF IS ", seat, hex(seat))
    seats.append(row)

changes_made = 1
while changes_made > 0:
    changes_made = 0
    seat_updates = []
    for row in range(len(seats)):
        row_updates = []
        for col in range(len(seats[row])):
            seatState = seats[row][col]
            if seatState == SeatState.EMPTY and NumberOfAdjacentOccupiedSeats(row, col) == 0:
                row_updates.append(SeatState.OCCUPIED)
                changes_made += 1
            elif seatState == SeatState.OCCUPIED and NumberOfAdjacentOccupiedSeats(row, col) >= 5:
                row_updates.append(SeatState.EMPTY)
                changes_made += 1
            else:
                row_updates.append(seatState)
        seat_updates.append(row_updates)
    
    seats = seat_updates
    ShowSeats()

occupied_seats = 0
for row in seats:
    for seat in row:
        if seat == SeatState.OCCUPIED:
            occupied_seats += 1

print("Occupied seats: ", occupied_seats)