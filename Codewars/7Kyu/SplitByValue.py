def split_by_value(k, elements):
    return sorted(elements, key=lambda x: x >= k) 

    # Another solution
    # small_num = []
    # large_num = []

    # for i in elements:
    #     if i < k:
    #         small_num.append(i)
    #     elif i >= k :
    #         large_num.append(i)


    # return small_num + large_num
        
        

print(split_by_value(1 , [9, 1]))