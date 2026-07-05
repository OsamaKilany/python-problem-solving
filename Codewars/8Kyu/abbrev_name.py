def abbrev_name(name):
    name = name.title().split()
    return f"{name[0][0]}.{name[1][0]}"




"""
    name = name.title().replace(" ", ".")
    for letter in name:
        if letter.islower():
            name = name.replace(letter, "")
    return name
"""

print(abbrev_name("Pinto Bean"))
