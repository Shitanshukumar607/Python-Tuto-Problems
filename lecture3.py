# Lecture 3
# List and tuples




## Problem 1
## WAP to ask the user to enter names of thier 3 fav movies & store them in a list


# movie1 = input("Enter first movie : ")
# movie2 = input("Enter second movie : ")
# movie3 = input("Enter third movie : ")

# movies = [movie1,movie2,movie3]

# print("Your favorite movies are" , movies)








## Problem 2
## WAP to check if a list contaains a palindrome of elements

# list1 = [1,2,3,2,1]
# list2 = [1,2,3,2,0]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# copy_list2 = list2.copy()
# copy_list2.reverse()

# if list1 == copy_list1:
#     print("List 1 is a palindrone")
# else:
#     print("List 1 is not a palindrone")

# if list2 == copy_list2:
#     print("List 2 is a palindrone")
# else:
#     print("List 2 is not a palindrone")







## Problem 3
## WAP to count the number of students with the "A" grade in the following tuple

# grades = ("C","D","A","A","B","B","A")

# occurance = grades.count("A")
# print("Occurance is",occurance)







## Problem 4
## Store the above values in a list & sort them from "A" ato "D"

grades = ["C","D","A","A","B","B","A"]
grades.sort()

print(grades)


