#addition

def add(*list):
    total = 0 
    #add all elements of the list

    for position in range (0,len(list)):
        total = total + list[position]

    return total

#multiplication

def multiply(*list):
    product = 1 

#multiply all elements of the list
    for x in range(0,len(list)):
        product *= list[x]

    return product