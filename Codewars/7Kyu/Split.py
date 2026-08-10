def split_by_mask(strng, mask):

    
    if sum(mask) != len(strng):
         return

    split_list = []
    tem = strng
    
    for i in mask:
        split_list.append(tem[:i])
        tem = tem[i:]
            
    return split_list  
    



print(split_by_mask("3B0b38d2DDe04C8eF6AC56E3A6", (15, 3, 1, 7)))   