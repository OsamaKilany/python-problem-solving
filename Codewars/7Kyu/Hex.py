HEX = set("0123456789ABCDEF")

def find_corrupted_byte(dump):
    for index in dump:
        cunr = set(index)
        print(cunr, HEX, sep="\n")

        for _ in range(2):
            if not cunr in HEX:
                return dump.index(index)
            


print(find_corrupted_byte(["48", "65", "6C", "6C", "6F"]))