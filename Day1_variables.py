# Variables in Python

age = 25
print(f"My age is {age}")
# --------------------------------------------------------------------------------------------  

x = "Sally" 
x = 4
print(x)

#  --------------------------------------------------------------------------------------------
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }
print(person_info)
print(skills)

# --------------------------------------------------------------------------------------------
first_name, last_name, country, age, is_married = 'Atharva', 'Admile', 'Nigeria', 250, True
print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

x=y=z=45
print(x,y,z)

# --------------------------------------------------------------------------------------------
"1. Check the data type of all your variables using type() built-in function"

print(type(skills))
print(type(person_info))
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(age))
print(type(is_married))

"2. Using the len() built-in function, find the length of your first name and your last name"

print(len(first_name))
print(len(last_name))

"3. The radius of a circle is 30 meters."
"Calculate the area of a circle and assign the value to a variable name of area_of_circle"
"Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle"
"Take radius as user input and calculate the area."

radius =30
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius
print(area_of_circle)
print(circum_of_circle)

radius2=int(input("enter radius"))
print(radius2)


