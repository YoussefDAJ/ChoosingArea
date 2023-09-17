area = input("Chose an area: (Cairo), (Alexandria), or (Tanta)\n")
if area.lower() == "cairo":
    print("You chose Cairo you can visit the pyramids")
elif area.upper() == "TANTA":
    print("Tanta is nice, but is hot at this time you need to be careful")
elif area.lower() == "alexandria":
    print("Feels like summer! Enjoy!")
else:
    print(f"Sorry, {area} is not on our list!")
