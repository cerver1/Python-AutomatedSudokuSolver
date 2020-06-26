from Sudoku_Site_Scraper import position_list
from Sudoku_Solver import board_solution, pre_solution
from Sudoku_Keyboard import keyboard_usage
from time import sleep
import re

mapped_board = []
solution_list = []
my_position_list = []
entry_list = []
entry_list_confirm = []


def board_mapping(board):
    for i in board_solution(board):
        mapped_board.append(i)

    for i in pre_solution:
        solution_list.append(str(mapped_board[i[0]][i[1]]))

    # convert positions to integer from string
    for i in position_list:
        my_position_list.append(int(i))

    for i in range(81):
        if i not in my_position_list:
            entry_list.append(i)

    for i in entry_list:
        entry_list_confirm.append('td{}'.format(i))


def empty_id(sqr_id, driver):
    sleep(0.5)
    empty = driver.find_element_by_xpath("//td[@id = '{}']".format(sqr_id))
    sleep(0.5)
    empty.click()


def value_entry(driver, solved):
    board_mapping(solved)

    sleep(1)
    driver.set_window_position(0, 0)
    sleep(1)

    for i in entry_list_confirm:
        empty_id(i, driver)
        sleep(0.5)
        keyboard_usage(driver, solution_list[entry_list_confirm.index(i)])
