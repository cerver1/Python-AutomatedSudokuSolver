from Sudoku_Site_Scraper import driver, position_list, wildcard
from Sudoku_Solver import board_solution,pre_solution
from Sudoku_Keyboard import keyboard_usage
from time import sleep
import re


mapped_board = []
solution_list = []
my_position_list = []
entry_list = []
entry_list_confirm = []

for i in board_solution():
    mapped_board.append(i)
    
for i in pre_solution:
    solution_list.append(str(mapped_board[i[0]][i[1]]))

print(solution_list)
print(len(solution_list))

# convert positions to integer from string
for i in position_list:
    my_position_list.append(int(i))


for i in range(0,81):
    if i not in my_position_list:
        entry_list.append(i)

print(my_position_list)
print(len(my_position_list))

for i in entry_list:
    entry_list_confirm.append('td{}'.format(i))

print(entry_list_confirm)
print(len(entry_list_confirm))

def empty_id(id):

    sleep(0.5)
    empty = driver.find_element_by_xpath("//td[@id = '{}']".format(id))
    sleep(0.5)
    empty.click()


# attempt = "2"
# keyboard_usage(attempt)

def value_entry():

    sleep(2)
    driver.set_window_position(0, 0)
    sleep(1)

    for i in entry_list_confirm:
        empty_id(i)
        sleep(0.5)
        keyboard_usage(solution_list[entry_list_confirm.index(i)])


value_entry()