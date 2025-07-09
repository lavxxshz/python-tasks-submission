#Task 1: Check if a Number is Even or Odd

num=int(input("Enter a number"))
if num%2==0:
    print(num,"is even")
else:
    print(num,"is odd")    

#    Task 2: Sum of Integers from 1 to 50 Using a Loop

for i in range(51):
    print(i)
total=sum(range(1,51))
print("1 to 50 additon is",total)