## SDSS Computing Studies Python Assignment
### Assignment #4 Using Input() (Total Marks 10)

Objectives:
* Use the input() function to retrieve information from the keyboard

To date, most of the data that we have used in Python has been assigned to variables using the variable assignment **=** operator.  However, it is also important to be able to receive input form the user while the program is running and to make use of that data. 

The input() command is used to do that.  It accepts 1 parameter inside the bracket. This is displayed as output, and then the program pauses and waits for data to be entered from the keyboard.  Pressing the Enter key signals the end of data and passes that information to the command.  It should then be assigned to a variable.  To see how this should be used, open up the example1.py file included with your assignment.

Note: the data received from an input() statement is always a string, and can't be used to enter a *float* or *int* type variable.  This is one of the reasons that *casting* a variable as another type is important.  We can use the following:

```
x = int(x)    # converts x into an integer
x = str(x)    # converts x into a string
x = float(x)  # converts x into a float
a = int(b)    # converts b into an integer and stores it into a new variable, a
```

You can also cast directly at the time that you retrieve your input:
```
x = int( input("Enter a number") )
Casting is very important if you want to retrieve a number from input and use it in a calculation.

**Important Note about the Autograder**
The autograder sometimes includes the ENTER key when it retrieves input.  This means that your input may have a hidden/unseen character that is attached to the end of your string literal.  If you cast it as a number, this is not a problem, however, it IS a problem for the autograder.  To correct this, we add the ".strip()" method to the end of your input to strip the hidden characters.

```
x = input("What is your name?").strip()

### 5 Tasks

**Note: Today you will be using Github Desktop to clone the repository to your local computer, and then commit all of the files at once**

##### Task 1
Ask the user for their name and their email address.\
Display the output back to the user in the following format:\
You will need to use the .strip() method for this assignment. Be aware of your punctuation!
```
Your name is Joe Lunchbox, and your email is joe@koolsandwiches.org.
```
(2 points) 

##### Task 2
Find the volume of a sphere.\
You will ask the user to enter the radius of the sphere.\
Calculate the Volume and then display the result to the user.\
You will need to import the *math* module in order to use *math.pi*\
Don't remember the formula for the volume of a sphere? You may need to look it up.
(2 points)

#### Task 3
Solve a two step algebra equation.\
Two steps equations are in the format *ax + b = c*\
You will ask the user to enter in all 3 variables: a, b and c\
You will need to display the solution for the equation
(2 points)

#### Task 4
Find the hypotenuse\
Your program will ask the user to enter in the 2 short sides of a right triangle.\
You will calculate the length of the hypotenuse and display the result.\
You will need to use the *math* module to use the command that finds the square root.\
(2 points)

#### Task 5
Find the radius of a sphere if you are given the volume.\
This is similar to task 2, but is the reverse!\
(2 points)
