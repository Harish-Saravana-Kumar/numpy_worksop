#write a program to find the sum of digits of a given number'

#solution

num = int(input("enter the number :"))
sum = 0
while num>0:
    rem = num % 10
    sum  += rem
    num //= 10

print(f"the sum is {sum}")
