names = ['ahmed', 'mohamed', 'mahmoud', 'moustafa', 'seleem']

print("The first three items in the list are: ")
for name in names[0:3]:
    print(name.title())

print("\nThree items from the middle of the list are: ")
for name in names[1:4]:
    print(name.title())

print("\nThe last three itesm in the list are: ")
for name in names[-3:]:
    print(name.title())