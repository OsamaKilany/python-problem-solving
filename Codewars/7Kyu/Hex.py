HEX = set("0123456789ABCDEF")

def find_corrupted_byte(dump):
    for index in dump:
        cur = set(index)
        if not cur in HEX:
                return dump.index(index)
           
    return -1





print(find_corrupted_byte(["48", "65", "6C", "6C", "6F"]))