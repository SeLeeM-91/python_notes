# Conditional tests examples
# False
age = 20
print("Is age < 20? I predict False.")
print(age < 20)

list = [2, 4, 6, 8]
print("Is 3 in list? I predict False.")
print(3 in list)

print("Is 4 is not in the list? I predict False.")
print(4 not in list)

name = 'AlEx'
print ("Is name == 'Alex' I predict False")
print(name.lower() == 'Alex')

age = 20
print("Is age < 20 or age > 20? I predict False")
print(age < 20 or age > 20)

# True
age = 20
print("Is age <= 20? I predict True.")
print(age <= 20)

list = [2, 4, 6, 8]
print("Is 3 not in list? I predict True.")
print(3 not in list)

print("Is 4 is in the list? I predict True.")
print(4 in list)

name = 'AlEx'
print ("Is name == 'Alex' I predict True")
print(name.title() == 'Alex')

age = 20
print("Is age < 20 or age == 20? I predict True")
print(age < 20 or age == 20)