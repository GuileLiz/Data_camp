#################################
###  Assigning to variables  ####
#################################
num1 = 7
num2 = 3
num1, num2 = 7, 3 #Multiple assignment
# Print command
print(num1 + num2)
# f-string 
print(f'The sum of {num1} + {num2} is {num1+num2}')
# Concatinating
print('The sum of',num1,'+',num2, 'is', num1+num2)

###################################
#### Type and Type conversion  ####
###################################	
# String
print(f"'5' is {type('5')}")
print(f"'3.14' is {type('3.14')}")
print(f"'True' is {type('True')}")
print('\n')
# Integer
print(f"-1 is {type(-1)}")
print(f" 6 is {type(6)}")
print('\n')
# Float
print(f"3.14 is {type(3.14)}")
print(f"1. is {type(1.)}")
print('\n')

################################
####   Method in String    #####
################################
name = ' guile '
print(name.title())   #convert str in title case
print(name.upper())   #convert str in lower case
print(name.lower())	  #convert str in upper case
print(name.rstrip())  #eliminate the white space at right
print(name.lstrip())  #eliminate the white space at left
print(name.strip())   #eliminate the white space at left and right

print('1'*3)          #If str is multiply to int, str will repeat based in int