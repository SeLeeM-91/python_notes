guest_list = ['solly', 'molly', 'bolly']
print(f"{len(guest_list)} Guests invetations:")
print (f"\tHello {guest_list[0].title()} you are invited to the dinner tomorrow!")
print (f"\tHey {guest_list[1].title()} lets have dinner tomorrow!")
print (f"\tHello {guest_list[2].title()} waiting you tomorrow for the dinner!")

print(f"\n### {guest_list[-1].title()} will not be able to attend")

guest_list[-1] = 'jully'
print(f"{len(guest_list)} Guests invetations:")
print (f"\tHello {guest_list[0].title()} you are invited to the dinner tomorrow!")
print (f"\tHey {guest_list[1].title()} lets have dinner tomorrow!")
print (f"\tHello {guest_list[2].title()} you are invited to the dinner tomorrow!")

print("\n### Hello all we have a new guests that will attend")

guest_list.insert(0, 'seleem')
guest_list.insert(2, 'ahmed')
guest_list.append('mostafa')
print(f"{len(guest_list)} Guests invetations:")
print (f"\tHello {guest_list[0].title()} you are invited to the dinner tomorrow!")
print (f"\tHello {guest_list[1].title()} you are invited to the dinner tomorrow!")
print (f"\tHello {guest_list[2].title()} you are invited to the dinner tomorrow!")
print (f"\tHello {guest_list[3].title()} you are invited to the dinner tomorrow!")
print (f"\tHello {guest_list[4].title()} you are invited to the dinner tomorrow!")
print (f"\tHello {guest_list[5].title()} you are invited to the dinner tomorrow!")

print("\n### I am so sorry there is an issue with the resturant i can only invite 2 members  we will arrange another one soon")

guest_name = guest_list.pop(0)
print (f"\t{guest_name} Sorry you are not invited this time")
guest_name = guest_list.pop()
print (f"\t{guest_name} Sorry you are not invited this time")
guest_name = guest_list.remove('jully')
print (f"\t{guest_name} Sorry you are not invited this time")
guest_name = guest_list.pop(1)
print (f"\t{guest_name} Sorry you are not invited this time")

print(f"{len(guest_list)} Guests invetations:")
print (f"\tHello {guest_list[0].title()} you are invited to the dinner tomorrow!")
print (f"\tHello {guest_list[1].title()} you are invited to the dinner tomorrow!")

del guest_list[1]
del guest_list[0]
print (f"\n remaining guest to invite: {len(guest_list)}")