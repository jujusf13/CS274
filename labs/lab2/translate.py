import math

def to_binary(quantity, from_base):
    # quantity: string we are converting
    # from_base: base we are converting from

    from_oct = {
        "0": "000",
        "1": "001",
        "2": "010",
        "3": "011",
        "4": "100",
        "5": "101",
        "6": "110",
        "7": "111"
    }

    from_hex = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }

    num_to_return = "" #change to num at end

    if (from_base == "octal"):
        num_to_return = ""
        for num in quantity:
            num_to_return += from_oct[num]

    elif from_base == "decimal":
        quantity = int(quantity)
        if quantity == 0:
            num_to_return = "0"
        else:
            squared_num = 1
            while squared_num * 2 <= quantity:
                squared_num *= 2

            counting = True
            while counting:
                if quantity >= squared_num:
                    num_to_return += "1"
                    quantity = quantity - squared_num
                else:
                    num_to_return += "0"

                if squared_num == 1:
                    counting = False
                squared_num //= 2

    elif (from_base == "hexadecimal"):
        num_to_return = ""
        for num in quantity:
            num_to_return += from_hex[num]

    return num_to_return




def to_octal(quantity, from_base):
    # quantity: string we are converting
    # from_base: base we are converting from

    from_binary = {
        "000": "0",
        "001": "1",
        "010": "2",
        "011": "3",
        "100": "4",
        "101": "5",
        "110": "6",
        "111": "7"
    }

    num_to_return = ""
    length = len(quantity)       

    #binary to octal
    if from_base == "binary":
        count = 0
        current_group = ""

        for num in reversed(quantity):
            current_group = num + current_group

            if count % 3 == 2:
                if current_group in from_binary:
                    num_to_return = from_binary[current_group] + num_to_return
                    current_group = ""
                else:
                    #print("error")
                    pass

            count += 1
            length -= 1

        if current_group:
            if len(current_group) == 2:
                current_group = "0" + current_group
                num_to_return = from_binary[current_group] + num_to_return
            elif len(current_group) == 1:
                current_group = "00" + current_group
                num_to_return = from_binary[current_group] + num_to_return

    #decimal to octal

    if from_base == "decimal":

        int_quantity = int(quantity)
        quantity_greater_than_eight = True
        quantity_num = int_quantity

        while quantity_greater_than_eight:
            if quantity_num <= 8:
                quantity_greater_than_eight = False
                num_to_return = str(math.floor(quantity_num)) + num_to_return
            else:
                quantity_num = quantity_num/8
                decimal_part = quantity_num - int(quantity_num)
                math.floor(quantity_num)
                remainder = decimal_part * 8
                remainder = int(remainder)
                remainder_str = str(remainder)
                num_to_return = remainder_str + num_to_return

    #Video I watched said to do it like this.
    if from_base == "hexadecimal":
        binary_num = to_binary(quantity, "hexadecimal")
        num_to_return = to_octal(binary_num, "binary")

    return num_to_return


def to_decimal(quantity, from_base):
    # quantity: string we are converting
    # from_base: base we are converting from

    from_hex = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "A": "10",
        "B": "11",
        "C": "12",
        "D": "13",
        "E": "14",
        "F": "15"
    }

    if (from_base == "binary"):
        #change from string to int for this one
        num_to_return = 0
        squares = 1
        for num in reversed(quantity):
            if num == "1":
                num_to_return += squares
            squares = squares * 2
        num_to_return = str(num_to_return)

    elif (from_base == "octal"):
        power = 0
        num_to_return = 0
        for num in reversed(quantity):
            num = int(num)
            num_to_return += num * (math.pow(8,power))
            power += 1
        num_to_return = str(num_to_return)

    elif (from_base == "hexadecimal"):
        num_to_return = 0
        power = 0

        for num in reversed(quantity):
            string_num = from_hex[num]
            #print("string_num:", string_num)
            num = int(string_num)
            num_to_return += num * (math.pow(16,power))
            power += 1
     
    return num_to_return


def to_hexadecimal(quantity, from_base):
    # quantity: string we are converting
    # from_base: base we are converting from

    from_binary = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
    }

    from_decimal = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F"
    }

    num_to_return = ""

    length = len(quantity)   
    if from_base == "binary":

        count = 0
        current_group = ""

        for num in reversed(quantity):
            current_group = num + current_group
            # print("current group:", current_group)
            # print("count:", count)

            if count % 4 == 3:
                if current_group in from_binary:
                    num_to_return = from_binary[current_group] + num_to_return
                    current_group = ""
                else:
                    #print("error")
                    pass

            count += 1
            length -= 1

        if current_group:
            if len(current_group) == 3:
                current_group = "0" + current_group
                num_to_return = from_binary[current_group] + num_to_return
            elif len(current_group) == 2:
                current_group = "00" + current_group
                num_to_return = from_binary[current_group] + num_to_return
            elif len(current_group) == 1:
                current_group = "000" + current_group
                num_to_return = from_binary[current_group] + num_to_return

    elif from_base == "octal":
        quantity = str(quantity)
        binary_num = to_binary(quantity, "octal")
        hexadecimal_num = to_hexadecimal(binary_num, "binary")
        num_to_return = hexadecimal_num

    elif from_base == "decimal":

        int_quantity = int(quantity)
        quantity_greater_than_sixteen = True
        quantity_num = int_quantity

        while quantity_greater_than_sixteen:
            if quantity_num < 16:
                quantity_greater_than_sixteen = False
                str_quantity_num = str(math.floor(quantity_num))

                num_to_return = from_decimal[str_quantity_num] + num_to_return
            else:
                quantity_num = quantity_num/16
                decimal_part = quantity_num - int(quantity_num)
                math.floor(quantity_num)
                remainder = decimal_part * 16
                remainder = int(remainder)

                remainder_str = str(remainder)
                remainder_str = from_decimal[remainder_str]
                num_to_return = remainder_str + num_to_return

    return num_to_return
