#                                                                                   Operators

1. Arithmetic Operators:

Addition(+): a + b
Subtraction(-): a - b
Multiplication(*): a * b
Division(/): a / b
Modulus(%): a % b
Floor division(//): a // b
Exponentiation(**): a ** b

2. Assignment operator:

=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3

3. Comparison Operator 

In programming we compare values, we use comparison operators to compare two values. We check if a value is greater or less or equal to other value.

==	Equal	x == y	

!=	Not equal	x != y	

>	Greater than	x > y

<	Less than	x < y	

>=	Greater than or equal to	x >= y	

<=	Less than or equal to	x <= y

In addition to the above comparison operator Python uses:

is: Returns true if both variables are the same object(x is y)
is not: Returns true if both variables are not the same object(x is not y)
in: Returns True if the queried list contains a certain item(x in y)
not in: Returns True if the queried list doesn't have a certain item(x in y)

4. Logical Operators
Unlike other programming languages python uses keywords and, or and not for logical operators. Logical operators are used to combine conditional statements.


and     	Returns True if both statements are true	               
x < 5 and  x < 10	
or	        Returns True if one of the statements is true	            
x < 5 or x < 4	
not	        7Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)

💻 Exercises - Day 2:

1. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

Base= int(input("Enter the base "))

Height =int(input("enter the Height "))

area_of_triangle=0.5*Base*Height

print(f"The area of the triangle is {area_of_triangle}")

2. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

a = int(input("enter the side a"))
b= int(input("enter the side b"))
c =int(input("enter the side c"))
perimeter_of_triangle=a+b+c
print(f"The perimeter of the triangle is {perimeter_of_triangle}")

3. Calculate the slope, x-intercept and y-intercept of y = 2x -2

# Define the equation y = mx + b
m = 2  # slope
b = -2  # y-intercept

# Calculate x-intercept (set y = 0)
x_intercept = -b / m

print("Slope (m):", m)
print("Y-intercept (b):", b)
print("X-intercept:", x_intercept)

4. Find the length of 'python' and 'dragon' and make a falsy comparison statement.

a= "python"
b="dragon"

print(len(a))
print(len(b))
print(a==b)

5. Use and operator to check if 'on' is found in both 'python' and 'dragon'

print("Python and Dragon has on: ", 'on' in 'Python and Dragon' )

6. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print( 'jargon' in 'I hope this course is not full of jargon')

7. Find the length of the text python and convert the value to float and convert it to string

# Step 1: Calculate the length of the text "python"
text = "python"
length = len(text)

# Step 2: Convert the length to a float
length_float = float(length)

# Step 3: Convert the float to a string
length_str = str(length_float)

# Output the results
print("Length as integer:", length)
print("Length as float:", length_float)
print("Length as string:", length_str)

8. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

a=int(input("enter number of years : "))
b=a*31536000
print(b)

#                                                                               Strings

Text is a string data type. Any data type written as text is a string. Any data under single, double or triple quote are strings. There are different string methods and built-in functions to deal with string data types. To check the length of a string use the len() method.

1. Escape Sequences in Strings
In Python and other programming languages \ followed by a character is an escape sequence. Let us see the most common escape characters:

\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")

2. String Interpolation / f-Strings (Python 3.6+)
Another new string formatting is string interpolation, f-strings. Strings start with f and we can inject the data in their corresponding positions.

3. Python Strings as Sequences of Characters
Python strings are sequences of characters, and share their basic methods of access with other Python ordered sequences of objects – lists and tuples. The simplest way of extracting single characters from strings (and individual members from any sequence) is to unpack them into corresponding variables.

4. Slicing Python Strings
In python we can slice strings into substrings.

5. Reversing a String
We can easily reverse strings in python.

6. Skipping Characters While Slicing
It is possible to skip characters while slicing by passing step argument to slice method.

7. String Methods
There are many string methods which allow us to format strings. See some of the string methods in the following example:

capitalize(): Converts the first character of the string to capital letter

count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.

endswith(): Checks if a string ends with a specified ending.

find(): Returns the index of the first occurrence of a substring, if not found returns -1.

rfind(): Returns the index of the last occurrence of a substring, if not found returns -1

💻 Exercises - Day 2

1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

a= 'thirty'
b='days'
c='of'
d='python'
print(a+' '+b+' '+c+' '+d)




