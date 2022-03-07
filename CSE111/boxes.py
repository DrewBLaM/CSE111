'''
A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. 
Write a Python program named boxes.py that asks the user for two integers: 
1) the number of manufactured items
2) the number of items that the user will pack per box. 
Your program must compute and print the number of boxes necessary to hold the items. 
This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.
'''

import math

#Collecting input from user
number_of_items = int(input('Please enter the number of items: '))
items_per_box = int(input('Please enter the number of items per box: '))
print()

#Math Calculations
number_of_boxes = math.ceil(number_of_items/items_per_box)

#Display Results
print(f'For {number_of_items}, packing {items_per_box} items in each box, you will need {number_of_boxes} boxes.')