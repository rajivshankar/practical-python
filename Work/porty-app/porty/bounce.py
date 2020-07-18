# bounce.py
#
# Exercise 1.5
initial_height = 100  # Height in metres
reduction_factor = 3/5 # in fractions

for i in range(10):
    initial_height = initial_height * reduction_factor
    print(i+1, round(initial_height, 4))
