from Sudoku_Url import selected_url
from Sudoku_Site_Scraper import go_to_site
from Sudoku_Solver import board_solution
from Sudoku_Site_Scraper_Entry import value_entry

# requests the difficulty level of the sudoku board and returns a generated board from livesudoku.com
empty_board = go_to_site(selected_url())

# enters the generated board into the sudoku solver algo and returns a solved board
solved_board = board_solution(empty_board[0])

# entries the board solution into the site sudoku board
value_entry(empty_board[1], solved_board)

''' 
To_Do_List

2. change relevant to list comprehension 

list = []

for i in range(9):
    list.append(i)
    
can be changed to 

out = [i for i in range(9)]

first value within the bracket is the value to be appended.

3. feature return and store solve time

'''
