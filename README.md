# **Automated Sudoku Solver**

### **Sometimes I get the urge to build projects that remind me of the wonder of coding, projects that don’t solve a pressing issue, projects that allow the exploration of the amazing world of programming.**

![](Sudoku_1.gif)

## ***Logic***

***

	This project uses python to solve a sudoku board on (Link - https://www.livesudoku.com/).

	This is achieved with the Selenium - webdriver, Time, and pynput libraries.

	How does it work?

	The id tag of all filled sudoku boxes and the values within the boxes are collected with the help of xpath and selenium.

	The id tags and values are used to draw a version of the sudoku board within the script

	The drawn board is then passed through a sudoku solver, finally returning a solution 

	This solution is then entered into the (Link - https://www.livesudoku.com/) site with the help of xpath, selenium and pynput.

***
***validateSAT():***
	
