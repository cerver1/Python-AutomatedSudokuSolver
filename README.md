# **Student Admission**

### **This program allows the entry of student data; this data is then calculated and graded through a point system. If the student accumulates over 100 points the student is admitted, else the student is denied.**

## ***Pseudocode***

***validateGPA():***

	if GPA.Input is between 2.0 and 4.0 :
    return Integer(GPA.text) * 20
	Else: Display Error “Please enter a valid GPA”
	
***validateSAT():***

	when(SAT):
  
	400..920 -> return 0
	930..1000 -> return 6
	1010..1190 -> return 10
	1200..1350 -> return 11
	1360..1600 -> return 12
	Else -> return “Please enter an SAT score between 400..1600”
	
***validateHighSchoolQuality():***

	when(Quality):
  
	0 -> return 0
	1 -> return 1
	2 -> return 4
	3 -> return 6
	4 -> return 8
	5 -> return 10
	
***validateDifficultyOfCurriculum():***

	when(Difficulty):
  
	-2 -> return -4
	-1 -> return -2
	0 -> return 0
	1 -> return 2
	2 -> return 4
	3 -> return 6
	4 -> return 8
	Else -> return “Please enter a Difficulty level between -2 and 4”
	
***validateGeography():***

	If Geography = State resident : return 10
	Else return 0
	
***validateEssayScore():***

	when(Essay):
  
	“Very Good” -> return 1
	“Excellent” -> return 2
	“Outstanding” -> return 3
	Else -> return “Please enter either “Very Good”, “Excellent”, or “ Outstanding”
	
***validateMiscellaneous():***

	when(Miscellaneous):
  
	“Socioeconomic disadvantage” or “Scholarship athlete” or “Provost’s discretion” -> return 20
	“Men in nursing” -> return 5
	Else -> return “Please enter “Socioeconomic disadvantage”, “Scholarship athlete”, “Provost’s discretion” or “Men in nursing””
	
***validateAlumni():***

	when(Alumni):
  
	“Legacy” -> return 4
	“Other” -> return 1
	Else -> return “Please enter “Legacy” or “Other
	
*Call all functions. If any function ends up within the Else argument, loop back to allow the
user to enter accurate information. If all functions are validated add all returned data from each.*

***validateStudent():***

    If returnedData <100 :
      print(“Congratulations this student is admitted with {returnedData} Points!”)
    Else:
      print(“I’m sorry this student has been denied due to {returnedData} Points!”)

![](Module1.jpg)
![](Module2.jpg)
![](Module3.jpg)
