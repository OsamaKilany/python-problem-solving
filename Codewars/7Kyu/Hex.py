HEX = set("0123456789ABCDEF")

def find_corrupted_byte(dump):
    for index in dump:
        for n in index:
            if not n in HEX or len(index) != 2:
                return dump.index(index)
    return -1
    
print(find_corrupted_byte(["48", "6", "6C"]))