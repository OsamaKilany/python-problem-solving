def introverted_seat(seats: str) -> str | None:



    if not '1' in seats or (seats[0] == '0' and seats[1]== ' '):
         return f"1{seats[1:]}"
    

    for index, seat in enumerate(seats): 
        if seat == '0' and not index == len(seats) - 1:
            if seats[index - 1] == ' ' and seats[index + 1] == ' ':
                return seats[:index] + '1' + seats[index + 1:]
            
    if seats[-1] == '0' and seats[-2]== ' ':
        return f"{seats[:-1]}1"
            
            
    if seats[0] == '0':
        return f"1{seats[1:]}"
            

    for index, seat in enumerate(seats):
        if seat == ' ':
            if seats[index - 1] == '0':
                return seats[:index - 1] + '1' + seats[index:]
            elif seats[index + 1] == '0':
                return seats[:index + 1] + '1' + seats[index + 2:] 
            
    if seats[len(seats)-1] == '0':
          return f"{seats[:len(seats)-1]}1"
 

    for index, seat in enumerate(seats):
        if seat == '1':
            continue
        elif seat == '0':
            if index - 1 == '0' and index + 1 == '0':
                return seats.repalce(index, '1')
   
print(introverted_seat('1010001 0'))
    