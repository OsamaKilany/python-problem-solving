def square_or_square_root(arr):
    square = []
    for i in arr:
        sq = i ** 0.5
        if sq % 1 != 0:
            square.append(i*i)
        else:
            square.append(sq)
            
    return square