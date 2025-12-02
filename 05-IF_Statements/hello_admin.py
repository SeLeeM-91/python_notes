users = ['Alex', 'Igor', 'Seleem', 'Admin', 'Petar']
if users:
    for user in users:
        if user == "Admin":
            print("Hello admin, whould you like to see a status report")
        else:
            print(f"Hello {user}, Thanks you for logging in again")
else:
    print("We need to find some users.")