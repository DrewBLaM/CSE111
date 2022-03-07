#datetime functionality
from datetime import datetime
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

#defining variables
loop = 1
sales_tax = .06
customer_subtotal = 0

#user input
while loop == 1:
    item_cost = float(input('Please enter the cost of your item! Press 0 when done: '))
    customer_subtotal = customer_subtotal + item_cost
    print(f'Total: ${customer_subtotal:.2f}')
    print()
    if item_cost == 0:
        loop = 0
print()
print()


#Discount days if/then
if day_of_week == 1 or day_of_week == 2:
    if customer_subtotal >= 50:
       discount = customer_subtotal * .10
       customer_subtotal = customer_subtotal - discount
    else:
        difference_for_discount = 50 - customer_subtotal 
        print(f'If you purchase an additional ${difference_for_discount:.2f} of items you are eligible for a 10% discount!')
        add_items = input('Would you like to add additonal items y/n? ')
        while add_items.lower() == 'y':
            item_cost = float(input('How much does the additional item cost? '))
            print()
            customer_subtotal = customer_subtotal + item_cost
            print(f'Your new subtotal is: ${customer_subtotal:.2f}')
            if customer_subtotal <= 50:
                difference_for_discount = 50 - customer_subtotal
                print(f'If you purchase an additional ${difference_for_discount:.2f} of items you are eligible for a 10% discount!')
            add_items = input('Would you like to add additional items y/n? ')
            print()
            print()
        if customer_subtotal >= 50:
            discount = customer_subtotal * .10
            customer_subtotal = customer_subtotal - discount
            print(f'You have received a ${discount:.2f} discount.')
            print()

#sales tax
sales_tax_amount = customer_subtotal * sales_tax

#Calculating total
final_bill = customer_subtotal + sales_tax_amount
print('--------------------')
print(f'Subtotal: ${customer_subtotal:.2f}')
print(f'Sales Tax: ${sales_tax_amount:.2f}')
print()
print(f'Total: ${final_bill:.2f}')
print('--------------------')
