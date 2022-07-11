#Jonathan.
#101161272

num1 = int(input("1. Enter a number: "))
num2 = int(input("2. Enter a number: "))
num3 = int(input("3. Enter a number: "))
num4 = int(input("4. Enter a number: "))

L = [num1,num2,num3,num4]
print(f"The largest difference is: {max(L)-min(L)}")