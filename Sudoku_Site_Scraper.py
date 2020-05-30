from Sudoku_Url import selected_url
from selenium import webdriver
from time import sleep
import re

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")   
chrome_options.add_argument('--ignore-certificate-errors') # This is to prevent the "Allow notification" dialog box which interferes with the code
chrome_options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=chrome_options)

position_list = []
position_list_value = []



def go_to_site():

    driver.get(selected_url())

    get_sudoku_board()
    
    sleep(2)
    


def get_sudoku_board():

    # empty_cord = driver.find_elements_by_xpath("//td[@class = 'cellnormal']")
    filled_cord = driver.find_elements_by_xpath("//span[@class = 'fixedcell']//parent::td[@class='cellnormal']")
    filled_cord_value = driver.find_elements_by_xpath("//span[@class = 'fixedcell']")
    
    for filled in filled_cord:
        position = extract_position(filled.get_attribute("id"), "td")
        position_list.append(position)
    
    for value in filled_cord_value:
        position_list_value.append(value.text)


def get_cord_position():

    for position in position_list:
        cord_position_column(position)

    sudoku_board = \
    [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def cord_position_column(position):

    row = cord_position_row(position)

    column = 9 * (row + 1) - position

    if column == 1:
        return (row,8)
    elif column == 2:
        return (row,7)
    elif column == 3:
        return (row,6)
    elif column == 4:
        return (row,5)
    elif column == 5:
        return (row,4)
    elif column == 6:
        return (row,3)
    elif column == 7:
        return (row,2)
    elif column == 8:
        return (row,1)
    elif column == 9:
        return (row,0)
    else:
        return print("something went wrong in your column")




def cord_position_row(position):
    
    if position in range(1,9):
        return 0
    elif position in range(9,18):
        return 1
    elif position in range(18,27):
        return 2
    elif position in range(27,36):
        return 3
    elif position in range(36,45):
        return 4
    elif position in range(45,54):
        return 5
    elif position in range(54,63):
        return 6
    elif position in range(63,72):
        return 7
    elif position in range(72,81):
        return 8
    else:
        return print("something went wrong in your row")



def extract_position(table_cord, prefix):
    return table_cord[table_cord.startswith(prefix) and len(prefix):]

'''
def when_statement_position(position):

    when_row = Switch({

        range(1,9): "1",
        range(9,18): 2,
        range(18,27): 3,
        range(27,36): 4,
        range(36,45): 5,
        range(45,54): 6,
        range(54,63): 7,
        range(63,72): 8,
        range(72,81): 9,

    })
    return when_row.get(position, "Something went wrong with your position")

class Switch(dict):
    def __getitem__(self, item):
        for key in self.keys():                   # iterate over the intervals
            if item in key:                       # if the argument is part of that interval
                return super().__getitem__(key)   # return its associated value
        raise KeyError(item)

print(when_statement_position(2))
'''
go_to_site()
print(len(position_list))
print(len(position_list_value))
# https://www.livesudoku.com/en/sudoku/easy/
# //td//span[@class = "fixedcell"]
