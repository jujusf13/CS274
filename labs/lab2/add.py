#########
######### ADDING METHODS
#########


def add(quantity_a, quantity_b, base):

    len_a = len(quantity_a)
    len_b = len(quantity_b)

    # Put this chunk of code back in loop if it does not work
    value = ""

    # This chunk is to add zeros to the front of the smaller
    # in length quantity

    zero_added_to_a = False
    if len_a >= len_b: # if same size or larger
        added_zeros = len_a - len_b
    else: 
        loop_value = quantity_b
        added_zeros = len_b - len_a
        zero_added_to_a = True #because a is less than b in length
    
    if not zero_added_to_a: # add to b
        for i in range(added_zeros):
            quantity_b = "0" + quantity_b
            len_b = len(quantity_b)
    else: #add to a
        for i in range(added_zeros):
            quantity_a = "0" + quantity_a
            len_a = len(quantity_a) #update values



    if base == "binary":
        # since same size now, just loop through the size of "a"

        carry = 0
        for i in range(len_a - 1, -1, -1):
            value_a = int(quantity_a[i])
            value_b = int(quantity_b[i])
            
            # adding
            sum_ab = value_a + value_b + carry
            if sum_ab == 0:
                value = "0" + value
                carry = 0
            elif sum_ab == 1:
                value = "1" + value
                carry = 0
            elif sum_ab == 2:
                value = "0" + value
                carry = 1
            elif sum_ab == 3:
                value = "1" + value
                carry = 1

            # carry if there is a leftover 1 after loop
        if carry == 1:
            value = "1" + value

    elif base == "octal":

        carry = 0
        for i in range(len_a - 1, -1, -1):
            value_a = int(quantity_a[i])
            value_b = int(quantity_b[i])
            
            sum_ab = value_a + value_b + carry
            if sum_ab < 8:
                value = str(sum_ab) + value
                carry = 0
            else:
                value = str(sum_ab - 8) + value
                carry = 1
            # Carry after loop is done if there is something to carry
        if carry == 1:
            value = "1" + value

    elif base == "decimal":
        quantity_a = int(quantity_a)
        quantity_b = int(quantity_b)
        value = quantity_a + quantity_b

    elif base == "hexadecimal":

        value = "" 
        carry = 0  
        for i in range(len_a - 1, -1, -1):
            value_a = int(quantity_a[i], 16) #convert hexa char to int
            value_b = int(quantity_b[i], 16)  
            
            sum_ab = value_a + value_b + carry
            if sum_ab < 16:
                value = format(sum_ab, 'x') + value  # Convert sum back to hexadecimal and add it to the front
                carry = 0 
            else:
                value = format(sum_ab - 16, 'x') + value  
                carry = 1

        # Carry after loop is done if there is something to carry
        if carry == 1:
            value = "1" + value

    return value
