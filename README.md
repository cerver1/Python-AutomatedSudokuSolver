# **Automated Sudoku Solver**

**Certain projects revitalize the urge to build for the sake of building. This project is one, it doesnt solve a pressing issue; this project simply allows for the exploration of the amazing world of programming.**

![](Sudoku_1.gif)

## Libraries
* Selenium - webdriver :gear:
* Time :clock1:
* pynput :computer:


## Project


### What?
	
	This project uses python to solve a random sudoku board found on https://www.livesudoku.com/

### How?

	The id tag of all filled sudoku boxes and the values within the boxes are collected with the help of xpath and selenium.

	The id tags and values are used to draw a version of the sudoku board within the script

	The drawn board is then passed through a sudoku solver, finally returning a solution 

	This solution is then entered into the https://www.livesudoku.com/ site with the help of xpath, selenium and pynput.
	
	
## Getting Started!
	
	- locally install all libraries
	- ensure libraries are working properly
	- clone repository
	- run the projuct from Sudoku_Main.py


### **:sun_with_face: Feel free to fork this repository and extend the capabilities of the project! :sun_with_face:**
	
