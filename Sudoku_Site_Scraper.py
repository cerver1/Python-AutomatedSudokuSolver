from Sudoku_Url import selected_url
from selenium import webdriver
from time import sleep
import re


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")   
chrome_options.add_argument('--ignore-certificate-errors') # This is to prevent the "Allow notification" dialog box which interferes with the code
chrome_options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=chrome_options)


def go_to_site():
    
    driver.get(selected_url())

    get_sudoku_board()
    
    sleep(2)
    


def get_sudoku_board():

    filled_cord = driver.find_elements_by_xpath("//td//span[@class = 'fixedcell']")
    
    for filled in filled_cord:
        print(filled.get_attribute("class"))
        # print(filled.text)


def get_cord_position():

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




go_to_site()

# https://www.livesudoku.com/en/sudoku/easy/
# //td//span[@class = "fixedcell"]
