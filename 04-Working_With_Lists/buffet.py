food = ('soup', 'salad', 'rice', 'chikecn', 'noodles')
print('Our buffet offers the following food today: ')
for food in food:
    print(f"\t{food.title()}")

# tupple is immutable cannot change items in it
#food[3] = 'Meat'
#   Traceback (most recent call last):
#        File "c:\Users\msele\OneDrive\Desktop\Python\4-Working_With_Lists\buffet.py", line 7, in <module>
#             food[3] = 'Meat'
#             ~~~~^^^
#       TypeError: 'str' object does not support item assignment

# writing over a tuple
food = 'soup', 'salad', 'rice', 'meat', 'jucie'
print("\nOur food for tomorrow will be: ")
for food in food:
    print(f"\t{food.title()}")
