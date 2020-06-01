from Sudoku_Site_Scraper import driver, position_list
from Sudoku_Solver import board_solution,pre_solution
from Sudoku_Keyboard import keyboard_usage
from selenium import webdriver
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
    solution_list.append(mapped_board[i[0]][i[1]])

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

id = 'td0'
sleep(2)
empty = driver.find_element_by_xpath("//td[@id = '{}']".format(id))
sleep(2)

empty.click()

sleep(2)

attempt = "2"
keyboard_usage(attempt)

    
