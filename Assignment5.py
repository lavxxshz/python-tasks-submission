#ASSIGNMENT 5:

#Module 6: Data Structures and Strings in Python

Studentrecord = {'Aman':78,'Rahul':76,'Sumesh':81}
name = input("Enter name whos record yoo want to featch")
if name in Studentrecord:
    print("student",name ,"and ther marks is ",Studentrecord[name])
else:
    print("Student not found")    


#Task 2: Demonstrate List Slicing 
numbers = list(range(1,11))
firstfive = numbers[:5]
reversedfive = firstfive[::-1]
print(firstfive)
print(reversedfive)
