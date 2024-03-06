# A290 Homework 8
# Your name here: _____Ronan Reddy______

# 1. Lambda
# Write an anonymous function to complete the task
# Given integer x and integer y. If x > 0, return x * y, else return x + y
# Choose reasonable numbers by yourself to test different cases
res = lambda x, y: x * y if x > 0 else x + y
print(res(1, 2)) 
print(res(-1, 2)) 

# 2. Comprehension
# Given a list of fruit names, using comprehension, create a new list containing only fruit with
# the letter 'e' in its name
# You MUST use comprehension to complete the task. With comprehension, there should be only one
# line of code to create the new list

fruits = ["apple", "banana", "cherry", "kiwi", "mango", "pineapple", "grape", "strawberry", "avocado"]

f = [i for i in fruits if 'e' in i]
print(f)



# 3. Plot
# Using numpy and matplotlib, plot the curve y = x^2 + 7x + 14
# The plot should at least display the curve where x ranges from [-20, 20]
# Hint: use np.arange() to create the range on the x-axis
# With np.arange, the "step" part of start-stop-step can be a float (ex: 0.1 instead of 1)
import numpy as np
import matplotlib.pyplot as plt

def curve(x):
    return x**2 + 7*x + 14
x = np.arange(-20, 20, 0.1)
y = curve(x)
plt.plot(x, y, label='y = x^2 + 7x + 14')
plt.xlabel('x')
plt.ylabel('y')
plt.show()





# Bonus fun thing (not a homework question): How to plot a heart
# Creating equally spaced 100 data in range 0 to 2*pi
theta = np.linspace(0, 2 * np.pi, 100)
# Generating x and y data
x = 16 * (np.sin(theta) ** 3)
y = 13 * np.cos(theta) - 5 * np.cos(2 * theta) - 2 * np.cos(3 * theta) - np.cos(4 * theta)
# Plotting
plt.plot(x, y)
plt.title('Heart!')
plt.show()