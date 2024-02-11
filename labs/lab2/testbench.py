import subtraction
import add
import translate

# All translating from one number type to another examples
print(translate.to_binary("10", "decimal"))  
print(translate.to_binary("37", "octal"))  
print(translate.to_binary("1F", "hexadecimal"))  

print(translate.to_octal("1010", "binary"))  
print(translate.to_octal("21", "decimal"))  
print(translate.to_octal("1F", "hexadecimal"))  

print(translate.to_decimal("1010", "binary"))  
print(translate.to_decimal("37", "octal"))  
print(translate.to_decimal("1F", "hexadecimal")) 

print(translate.to_hexadecimal("1010", "binary"))  
print(translate.to_hexadecimal("37", "octal"))  
print(translate.to_hexadecimal("21", "decimal"))  

# Subtraction examples
print("")
print(subtraction.sub("1001", "0110", "binary", "")) 
print(subtraction.sub("37", "27", "octal", "")) 
print(subtraction.sub("21", "19", "decimal", ""))
print(subtraction.sub("1F", "B", "hexadecimal", ""))

print("")
print(add.add("10", "10", "binary"))
print(add.add("70", "13", "octal"))
print(add.add("37", "42", "decimal"))
print(add.add("AF", "9D", "hexadecimal"))