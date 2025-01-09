#                                                                               Conditionals
# if condition 
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number


# if-else condition
# If condition is true the first block will be executed, if not the else condition will run.
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# if-elif-else condition
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# Nested Condition 
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# If Condition and Logical Operators
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# If and Or Logical Operators
user = 'James'
access_level = int(input("What is your access level"))
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')



    
