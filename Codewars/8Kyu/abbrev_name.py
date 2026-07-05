def abbrev_name(name):
    name = name.title().replace(" ", ".")
    for letter in name:
        if letter.islower():
            name = name.replace(letter, "")
    return name


print(abbrev_name("Pinto Bean"))
