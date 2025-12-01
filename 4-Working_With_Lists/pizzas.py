pizzas = ['chicken', 'pepproni', 'c-food']
# for pizza in pizzas:
#     print (f"I love {pizza.title()} pizza")
# print("\nI really love pizza!\n")

friend_pizzas = pizzas[:]

pizzas.append("Cheese")
print("My favorite pizzas are: ")
for pizza in pizzas:
    print(f"\t{pizza.title()}")

friend_pizzas.append("roman")
print("\nMy friend favorite pizzas are: ")
for pizza in friend_pizzas:
    print(f'\t{pizza.title()}')

# Wrong copy example
languages = ['english', 'arabic', 'Chinese']
friend_languages = languages
languages.append('spanish')
friend_languages.append('hindi')

print('My languages are: ')
for language in languages:
    print(f"\t{language.title()}")

print('\nMy friend languages are: ')
for language in friend_languages:
    print(f"\t{language.title()}")