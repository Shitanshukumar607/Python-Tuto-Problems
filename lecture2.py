# Lecture 2
# Strings and conditional statements




## Problem 1
## WAP to input user's first name and print its length


# name = input("Enter your name : ")
# length = len(name)

# print("Length is" , length)








## Problem 2
## WAP to find the occurance of "$" in a string


# name = input("Enter the string : ")
# occurance = name.count("$")

# print("Occurance is", occurance)








## Problem 3
## WAP to find if the number entered by user is even or odd


# num = int(input("Enter the number : "))

# if (num % 2 ) == 0:
#     print("The number is even")
# else :
#     print("The number is odd")









## Problem 4
## WAP to find the greatest of 3 nums entered by the user

# a = int(input("First number : "))
# b = int(input("Second number : "))
# c = int(input("Third number : "))

# if a >= b and a >= c:
#     print("The first number is the highest")
# elif b >= c :
#     print("The second number is the highest")
# else :
#     print("The third number is the highest")







## Problem 5
## WAP to check if a num is a multiple of 7 or not

num = int(input("First number : "))


if num % 7 == 0:
    print("A multiple")
else :
    print("Not a multiple")
