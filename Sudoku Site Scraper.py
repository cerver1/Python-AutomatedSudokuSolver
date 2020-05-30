'''
from selenium import webdriver
from time import sleep
import re


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")   
chrome_options.add_argument('--ignore-certificate-errors') # This is to prevent the "Allow notification" dialog box which interferes with the code
chrome_options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=chrome_options)

'''


def request_difficulty_level():
    difficulty_scale = '\n1 = Easy\n2 = Medium\n3 = Hard\n4 = Evil\n\n'
    difficulty = input("{}Please enter a number that corresponds to a difficulty level: ".format(difficulty_scale))

    if int(difficulty) not in range(1, 5):
        request_difficulty_level()
    else:
        continue_prompt(difficulty)


def continue_prompt(difficulty):

    when = {
        1: "\nYour selected: Easy, do you want to continue? (Y\N): ",
        2: "\nYour selected: Medium, do you want to continue? (Y\N): ",
        3: "\nYour selected: Hard, do you want to continue? (Y\N): ",
        4: "\nYour selected: Evil, do you want to continue? (Y\N): "
    }

    confirm = str(raw_input(when.get(difficulty)))
    if confirm.upper() == "Y":
        print("continue")
    elif confirm.upper() == "N":
        request_difficulty_level()
    else:
        continue_prompt(difficulty)


request_difficulty_level()

'''
def go_to_site(difficulty):

    
    driver.get('https://www.websudoku.com/?level='+ difficulty)
    sleep(5)

    get_sudoku_board(get_cord_list())
    
    sleep(2)
    

def get_cord_list():

    list_of_cords = []

    for i in range(0,89):
        if len(str(i)) == 1:
            list_of_cords.append('f0'+ str(i))
        else:
            list_of_cords.append('f'+ str(i))

    return list_of_cords

def get_sudoku_board(cord_list):

    for cord in cord_list:

        found_cord = driver.find_element_by_xpath("//input[@id = \'"+ cord +"\']")
        
        if found_cord.get_attribute('@class') == 's0':
            print('filled')
        elif found_cord.get_attribute('@class') == 'd0':
            print('empty')

# request_difficulty_level()

site = driver.get('https://www.livesudoku.com/en/sudoku/easy/')
sleep(20)
'''
# https://www.livesudoku.com/en/sudoku/easy/
# //td//span[@class = "fixedcell"]
