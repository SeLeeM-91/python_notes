fav_number = {
    'igor': 5,
    'aleksandar': 30,
    'petar': 60,
    'ahmed': 100,
    'seleem': 91,
}
print(f"The favorite number for Igor is {fav_number['igor']}")
print(f"The favorite number for Alekandar is {fav_number['aleksandar']}")
print(f"The favorite number for Petar is {fav_number.get('petar')}")
print(f"The favorite number for Ahmed is {fav_number['ahmed']}")
print(f"The favorite number for Seleem is {fav_number.get('seleem')}")