from enum import Enum

with open('/Users/matt/Projects/Advent of Code/2020/aoc-day11-input.txt') as my_file:
    seat_rows = my_file.readlines()

class SeatState(Enum):
    FLOOR = 0
    EMPTY = 1
    OCCUPIED = 2

seats = []

def NumberOfAdjacentOccupiedSeats(row, col):
    global seats
    count = 0
    for rowOffset in [-1, 0, 1]:
        for colOffset in [-1, 0, 1]:
            
            # Skip the seat itself
            if rowOffset == 0 and colOffset == 0:
                continue

            if row + rowOffset < 0 or row + rowOffset >= len(seats):
                continue

            if col + colOffset < 0 or col + colOffset >= len(seats[row]):
                continue

            try:
                if seats[row+rowOffset][col+colOffset] == SeatState.OCCUPIED:
                    count += 1
            except IndexError as identifier:
                print(identifier)
    
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
            elif seatState == SeatState.OCCUPIED and NumberOfAdjacentOccupiedSeats(row, col) >= 4:
                row_updates.append(SeatState.EMPTY)
                changes_made += 1
            else:
                row_updates.append(seatState)
        seat_updates.append(row_updates)
    
    seats = seat_updates
    #ShowSeats()

occupied_seats = 0
for row in seats:
    for seat in row:
        if seat == SeatState.OCCUPIED:
            occupied_seats += 1

print("Occupied seats: ", occupied_seats)