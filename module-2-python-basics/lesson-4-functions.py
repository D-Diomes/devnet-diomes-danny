"""
Module 2 — Lesson 4: Functions
Student: Diomes, Danny D.
Date: September 28, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
A function is a block of code that is made to do a specific task.
Instead of writing the same code again and again, I can put it inside a function and use the function whenever I need it.

I think of a function like a machine. I can give it some information, it does a task, and it can give me a result back. 
A function can also have parameters, which are values that I give to the function.

============================================
KEY VOCABULARY
============================================
- function: A reusable block of code that performs a specific task.
- def: A keyword used in Python to create or define a function.
- parameter: A variable inside the function definition that receives a value.
- argument: The actual value that I give to a function when I call it.
- return: Sends a value back from the function.
- function call: Using the function so that the code inside it runs.

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

def calculate_average(score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    return average

result = calculate_average(85, 90, 88)

print(f"Average: {result}")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is forgetting to use return when I want a function to give a result back.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""