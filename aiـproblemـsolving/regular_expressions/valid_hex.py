import re

def is_valid_hex(string):
    return bool(re.search(r"^#([a-f0-9]{3}|[a-f0-9]{6})$", string, re.IGNORECASE))

print(is_valid_hex("#fff"))