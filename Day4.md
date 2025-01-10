#                                                                               Randomization
Randomization in Python is handled using the random module, which provides various methods to generate random numbers or make random selections.

Randomisation refers to generating random numbers or selecting random elements from a sequence. In Python, randomisation is primarily facilitated by the random module, which provides a variety of functions for working with random data.

#
1. Importing the random module :

       import random

2. Generating random numbers

       random.random()
Generates a random float number between 0.0 and 1.0.

         print(random.random())  # Example: 0.845421326

--> random.uniform(a, b)

Generates a random float number between a and b.

      print(random.uniform(10, 20))  # Example: 15.6782

--> random.randint(a, b)

Generates a random integer between a and b (inclusive).

      print(random.randint(1, 10))  # Example: 7

3. Random selection

-->random.choice(seq)

Selects a random item from a non-empty sequence.

    fruits = ['apple', 'banana', 'cherry']
    print(random.choice(fruits))  # Example: banana
--> random.choices(seq, weights=None, k=1)

Selects k random items from the sequence, with optional weights.
   
     print(random.choices(fruits, weights=[1, 2, 1], k=3))  # Example: ['banana', 'apple', 'banana']

--> random.sample(seq, k)

Selects k unique items from the sequence (without replacement).
 
    print(random.sample(fruits, 2))  # Example: ['apple', 'cherry']

4. Shuffling data

--> random.shuffle(seq)

Shuffles a mutable sequence (e.g., a list) in place.

     cards = [1, 2, 3, 4, 5]
    random.shuffle(cards)
    print(cards)  # Example: [4, 1, 3, 5, 2]
#
Example: Simple Dice Roll Simulation
 
    import random

    def roll_dice():
    return random.randint(1, 6)

    print(f"You rolled a {roll_dice()}!")

#                                                                               Lists

Lists in Python are one of the most versatile and widely used data structures. They are ordered, mutable (modifiable), and allow duplicate elements. 
#
1. Creating a List

Empty list:

    my_list = []
List with elements:

    numbers = [1, 2, 3, 4, 5]
    fruits = ["apple", "banana", "cherry"]
    mixed = [1, "hello", 3.5, True]

2. Accessing Elements

Indexing:
    
    print(fruits[0])  # Output: apple
    print(fruits[-1]) # Output: cherry (negative index starts from the end)
Slicing:

    print(numbers[1:4])  # Output: [2, 3, 4]
    print(numbers[:3])   # Output: [1, 2, 3]
    print(numbers[::2])  # Output: [1, 3, 5]

3. Modifying a List

Changing values:
 
    fruits[1] = "orange"
    print(fruits)  # Output: ['apple', 'orange', 'cherry']
Adding elements:

Append:

    fruits.append("grape")
    print(fruits)  # Output: ['apple', 'orange', 'cherry', 'grape']
Insert:
  
    fruits.insert(1, "blueberry")
    print(fruits)  # Output: ['apple', 'blueberry', 'orange', 'cherry']
Removing elements:

Remove by value:

    fruits.remove("orange")
    print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

#
Lists Documentation

You can find the documentation for Python Lists and other List related functions here: https://docs.python.org/3/tutorial/datastructures.html