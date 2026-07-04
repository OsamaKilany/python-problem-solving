def enough(cap, on, wait):
    if wait >= (cap-on):
        return wait - (cap-on) 
    else:
        return 0
    
print(enough(20, 19, 5))