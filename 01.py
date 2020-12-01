import copy
from pathlib import Path

input=(Path(__file__).parent/"01_input.txt").read_text().split("\n")

input=[int(i) for i in input if i.strip() != ""]

def puzzle_1(input):
    burn_down_list=copy.deepcopy(input)
    while len(burn_down_list) > 0:
        i=burn_down_list.pop()
        for j in burn_down_list:
            if (i+j)==2020:
                print(f'{i} * {j} = {i*j}')
def puzzle_2(input):
    burn_down_list=copy.deepcopy(input)
    while len(burn_down_list) > 0:
        i=burn_down_list.pop()
        burn_down_list_2=copy.deepcopy(burn_down_list)
        while len(burn_down_list_2) > 0:
            j=burn_down_list_2.pop()
            if i+j < 2020:
                for k in burn_down_list_2:
                    if (i+j+k)==2020:
                        print(f'{i} * {j} * {k} = {i*j*k}')
puzzle_1(input)
puzzle_2(input)