from Sudoku_Url import selected_url
from Sudoku_Site_Scraper import go_to_site
from Sudoku_Solver import board_solution
from Sudoku_Site_Scraper_Entry import value_entry

# requests the difficulty level of the sudoku board and returns a generated board from livesudoku.com
empty_board = go_to_site(selected_url())

# enters the generated board into the sudoku solver algo and returns a solved board
solved_board = board_solution(empty_board[0])

# enteres the board solution into the site sudoku board
value_entry(empty_board[1], solved_board)