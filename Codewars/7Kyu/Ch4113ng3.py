def nerdify(txt):
       
    if 'l' in txt:
        txt= txt.replace('l', '1')
    
    for char in txt:
        if char in "Aa":
            txt = txt.replace(char, '4')
        elif char in 'Ee':
            txt = txt.replace(char, '3')

    return txt


print(nerdify("Fund4ment41s"))