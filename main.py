Sayings = {
    "Blood is thicker than water" : "Blood of the covenant is thicker than the water of the womb",
    "Curiosity killed the cat": "Curiosity killed the cat, but satisfaction brought it back",
    "Jack of all trades, master of none" : "Jack of all trades, master of none but better than a master of one",
    "The early bird catches the worm" : "The early bird catches the worm, but the sacond mouse gets the cheese"
}

unknown = input("Input a saying which might be cut down:")

if unknown in Sayings.keys():
    print(Sayings[unknown])
else:
    add = input("This is not on the list. Do you want to add it?")
    if add == "yes":
        new_value = input("Enter the full saying:")
        Sayings[unknown] = new_value
        print(Sayings[unknown], "has been added.")
