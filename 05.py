
"""
--- Day 5: Binary Boarding ---

You board your plane only to discover a new problem: you dropped your boarding 
pass! You aren't sure which seat is yours, and all of the flight attendants are 
busy with the flood of people that suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby 
boarding passes (your puzzle input); perhaps you can find your seat through 
process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat 
people. A seat might be specified like FBFBBFFRLR, where F means "front", B means 
"back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 
128 rows on the plane (numbered 0 through 127). Each letter tells you which half 
of a region the given seat is in. Start with the whole list of rows; the first 
letter indicates whether the seat is in the front (0 through 63) or the back (64 
through 127). The next letter indicates which half of that region the seat is in, 
and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
The last three characters will be either L or R; these specify exactly one of the 
8 columns of seats on the plane (numbered 0 through 7). The same process as above 
proceeds again, this time with only three steps. L means to keep the lower half, 
while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. 
In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
As a sanity check, look through your list of boarding passes. What is the highest 
seat ID on a boarding pass?

Your puzzle answer was 866.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding 
pass in your list. However, there's a catch: some of the seats at the very front 
and back of the plane don't exist on this aircraft, so they'll be missing from 
your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 
from yours will be in your list.

What is the ID of your seat?

Your puzzle answer was 583.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

import copy
import json
from pathlib import Path


input=(Path(__file__).parent/"05_input.txt").read_text().split("\n")
input=[i.strip() for i in input if i.strip()!= ""]



def get_row(row_code:str):
    assert len(row_code)==7
    start=0
    end=128
    for i in range(7):
        span=end-start
        half_span=int(span/2)
        # print(f'{i} {row_code[i]} {start} {end} of {span} next {half_span}')
        if row_code[i]=='F':
            start=start
            end = end - half_span
        else:
            start=start + half_span
            end = end
        # print(f'{i} {row_code[i]} {start} {end}')
    return end - 1

def get_seat(seat_code:str):
    assert len(seat_code)==3
    start=0
    end=8
    for i in range(3):
        span=end-start
        half_span=int(span/2)
        # print(f'{i} {seat_code[i]} {start} {end} of {span} next {half_span}')
        if seat_code[i]=='L':
            start=start
            end = end - half_span
        else:
            start=start + half_span
            end = end
        # print(f'{i} {seat_code[i]} {start} {end}')
    return end - 1

def get_seat_id(seat_code:str):
    assert len(seat_code)==10
    row=seat_code[:7]
    seat=seat_code[-3:]
    #print(row, seat)
    return get_row(row) * 8 + get_seat(seat)


assert get_seat_id('BFFFBBFRRR') == 567
assert get_seat_id('FFFBBBFRRR') ==119
assert get_seat_id('BBFFBBFRLL') ==820
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.

assert get_row("FBFBBFF") == 44
assert get_row("BFFFBBF") == 70
assert get_row("FFFBBBF") == 14
assert get_row("BBFFBBF") == 102

assert get_seat("RLR") == 5
assert get_seat("RRR") == 7
assert get_seat("RLL") == 4

def puzzle_1(input):
    max_seat_id=0
    for i in input:
        max_seat_id=max(get_seat_id(i), max_seat_id)
    return max_seat_id


def puzzle_2(input):
    max_seat_id=0
    all_seats = []
    for i in input:
        all_seats.append(get_seat_id(i))
    all_seats.sort()
    #print(all_seats)
    my_seat=None
    for seat in all_seats:
        if seat + 1 not in all_seats:
            if seat +2 in all_seats:
                assert my_seat is None
                my_seat = seat+1
    
    return my_seat


print(f'PUZZLE 1: {puzzle_1(input)}')
print(f'PUZZLE 2: {puzzle_2(input)}')
