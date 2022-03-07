import math

'''
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. 
The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits. 

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
'''

w = float(input('Please enter the width of the tire in mm (ex 205): '))
a = float(input('Please enter the aspect ratio of the tire (ex 60): '))
d = float(input('Please enter the diameter of the tire in inches (ex 15): '))

v = ((math.pi*a*w**2)*((w*a)+d*2540))/10000000000

print(f'The approximate volume is {v:.2f} liters')