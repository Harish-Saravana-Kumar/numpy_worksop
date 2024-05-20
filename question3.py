#write a program to find the factorial of a nummber

# solution

def fact(a):
    if a == 1:
        return 1
    else:
        return a * fact(a-1)
     
a = int(input("enter the number:"))
b = fact(a)
print(f"the number is {b}")