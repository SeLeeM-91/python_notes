current_users = ['Alex', 'Igor', 'Seleem', 'Admin', 'Petar']
new_users = ['john', 'hulk', 'Seleem', 'Admin', 'luffy']

current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"sorry {new_user}, this username is already in use.")
    else:
        print(f"Ok {new_user}, this username is avilable.")