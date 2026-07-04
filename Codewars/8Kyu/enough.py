def enough(cap, on, wait):
    if wait + on == cap:
        return 0
    else:
        return wait - (cap-on)
        
    
print(enough(20, 19, 5))