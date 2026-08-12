# print("This program checks whether a number is even or odd")

# number = int(input("Enter a number: "))
#     print ("You entered a valid number")
#     print ("You entered an invalid number")
# modulo = number % 2
# print("The modulo of", number, "is", modulo)
# if modulo == 0:
#     print(number, "is an even number")
# else:
#     print(number, "is an odd number")
    
try:
    number = int(input("Enter a number: "))
  
    modulo = number % 2
    print("The modulo of", number, "is", modulo)

    if modulo == 0:
        print(number, "is an even number")
    else:
        print(number, "is an odd number")

except ValueError:
    print("You entered an invalid number")