#Task 1: Read a File and Handle Errors 
file1=open('sample.txt','r')
file_oppening =file1.read()
print(file_oppening)
file1.close()

#Task 2: Write and Append Data to a File

file2 = open('output.txt','w')
n=input("Enter what you want to display or dave in txt file")
file_opening=file2.write(n)
file2.close()
print('adding data succesfull')

file2= open('output.txt','r')
file_opening1=file2.read()
print(file_opening1)
file2.close()
            
