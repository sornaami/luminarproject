# Program to check if a number is prime or not

num=int(input("enter number"))
for i in range(2,num):
    if (num%i==0):
        print(num, "is not a prime number")
        break
    else:
        print(num, "is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime

