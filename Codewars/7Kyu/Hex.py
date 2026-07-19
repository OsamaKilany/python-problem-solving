HEX = set("0123456789ABCDEF")

def find_corrupted_byte(dump):
    for index in dump:
        if not index in HEX:
            if index.isalnum() and index.isupper():
                return dump.index(index)
            return dump.index(index)
    return -1





print(find_corrupted_byte(["48", "65", "6C", "6C", "6F"]))