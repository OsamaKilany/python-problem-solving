def nerdify(txt):
       
    if 'l' in txt:
        txt= txt.replace('l', '1')
        
    txt = txt.lower()
    
    if "e" in txt:
        txt = txt.replace('e', '3')
    if "a" in txt:
        txt =txt.replace('a', '4')
    
    return txt.capitalize()



print(nerdify("Fundamentals"))