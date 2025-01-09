#                                                                                 Conditionals 
1. Conditional execution: a block of one or more statements will be executed if a certain expression is true
2. Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover if, else, elif statements. The comparison and logical operators we learned in previous sections will be useful here.

1. If Condition :
In python and other programming languages the key word if is used to check if a condition is true and to execute the block code. Remember the indentation after the colon.

-->Syntax
if condition:
    this part of code runs for truthy conditions

2. If Else : 
If condition is true the first block will be executed, if not the else condition will run.

-->Syntax
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions

3. If Elif Else :
In our daily life, we make decisions on daily basis. We make decisions not by checking one or two conditions but multiple conditions. As similar to life, programming is also full of conditions. We use elif when we have multiple conditions.

-->Syntax
if condition:
    code
elif condition:
    code
else:
    code

4. Nested Conditions :
Conditions can be nested

-->Syntax
if condition:
    code
    if condition:
    code

5. If Condition and Logical Operators

-->Syntax
if condition and condition:
    code

6. if and Or Logical Operators
-->Syntax
if condition or condition:
    code

💻 Exercises: Day 3

1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 

Code :

age = int(input('Enter your age: '))

if age >= 18:
    print('You are old enough to drive')
else:
    years_left = 18 - age
    print(f'You are not old enough to drive Please wait {years_left} years')

2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

Code :

my_age = int(input("How old are you?"))
your_age = int(input("How old are you?"))
if my_age == your_age:
    print("We are the same age")
elif my_age > your_age:
    years_left = my_age - your_age
    print(f"You are {years_left} years older than me")
else:
    years_left = your_age - my_age
    print(f"You are {years_left} years younger than me")

3. Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F

Code:

score = int(input('Enter your score: '))
if score >= 80:
    print('A')
elif score >= 70:
    print('B')
elif score >= 60:
    print('C')
elif score >= 50:
    print('D')
else:
    print('fail')


4. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

Code:
month = input("Enter a Month: ")
if month == "September" or month == "October" or month == "November":
    print("The season is Autumn")
elif month == "December" or month == "January" or month == "February":
    print("The season is Winter")
else :
    month == "March" or month == "April" or month == "May"
    print("The season is Spring")

