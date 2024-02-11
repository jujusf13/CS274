from translate import to_binary, to_hexadecimal, to_octal, to_decimal


#was not able to do this for base 1
def sub(quantity_a, quantity_b, base, mode):

    value = 0

    len_a = len(quantity_a)
    len_b = len(quantity_b)

    # Put this chunk of code back in loop if it does not work
    value = ""

    # this chunk is to add zeros to the front of the smaller
    # in length quantity

    zero_added_to_a = False
    if len_a >= len_b: # if same size or larger
        added_zeros = len_a - len_b
    else: 
        loop_value = quantity_b
        added_zeros = len_b - len_a
        zero_added_to_a = True 
    
    if not zero_added_to_a: # add to b
        for i in range(added_zeros):
            quantity_b = "0" + quantity_b
            len_b = len(quantity_b)
    else: #add to a
        for i in range(added_zeros):
            quantity_a = "0" + quantity_a
            len_a = len(quantity_a) #update values

    # and if mode is not base1
    if base == "binary":

        value = "" 
        borrow = 0  
        for i in range(len_a - 1, -1, -1):
            value_a = int(quantity_a[i])
            value_b = int(quantity_b[i])

            # subtract with borrow here
            diff_ab = value_a - value_b - borrow #borrow is subtracted because if we borrowed from
            # the left on the previous part of the problem, when we are now currently at that number,
            # it has to be one less than it was before. And we subtract that from the total of a-b.
            if diff_ab >= 0:
                value = str(diff_ab) + value
                borrow = 0 
            else:
                value = str(diff_ab + 2) + value  # add 2 to make the difference positive
                borrow = 1 

    elif base == "octal":

        value = ""  
        borrow = 0  
        for i in range(len_a - 1, -1, -1):
            value_a = to_decimal(quantity_a[i], "octal")
            value_a = float(value_a)  
            value_a = int(value_a)

            value_b = to_decimal(quantity_b[i], "octal")
            value_b = float(value_b)  
            value_b = int(value_b)

            diff_ab = value_a - value_b - borrow
            if diff_ab >= 0:
                value = str(diff_ab) + value
                borrow = 0
            else:
                value = str(diff_ab + 8) + value  # add 8 to make difference positive and borrow a 1
                borrow = 1 

    elif base == "decimal":
        value_a = int(quantity_a)
        value_b = int(quantity_b)
        if value_a >= value_b:
            value = value_a - value_b
        else:
            value = value_b - value_a

    elif base == "hexadecimal":

        value = ""  
        borrow = 0  
        for i in range(len_a - 1, -1, -1):
            value_a = to_decimal(quantity_a[i], "hexadecimal")
            value_a = float(value_a)  
            value_a = int(value_a)

            value_b = to_decimal(quantity_b[i], "hexadecimal")
            value_b = float(value_b)  
            value_b = int(value_b)

            diff_ab = value_a - value_b - borrow
            if diff_ab >= 0:
                value = str(diff_ab) + value
                borrow = 0
            else:
                value = str(diff_ab + 16) + value  # add 8 to make difference positive and borrow a 1
                borrow = 1 

    return value

