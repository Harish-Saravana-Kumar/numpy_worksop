# find if the given number is a palindrome or not?

#solution
a = int(input("enter the number:"))
a = str(a)
if a[::-1] == a :
    print("it is palindrome")
else :
    print("it is not a palindrome")
