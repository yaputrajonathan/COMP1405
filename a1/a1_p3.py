#Jonathan.
#101161272

print("Please enter your grade on the following pieces of work:")
assignment1 = int(input("Assignment 1 (/18): "))
assignment2 = int(input("Assignment 2 (/22): "))
assignment3 = int(input("Assignment 3 (/15): "))
assignment4 = int(input("Assignment 4 (/30): "))
midterm = int(input("Midterm (/35): "))
final = int(input("Final Exam (/50): "))
print("")

print("Your grades:")
print("-"+"="*21+"-")

print(f"Assignment 1     {assignment1/18*100:.2f}%")
print(f"Assignment 2     {assignment2/22*100:.2f}%")
print(f"Assignment 3     {assignment3/15*100:.2f}%")
print(f"Assignment 4     {assignment4/30*100:.2f}%")
print(f"Midterm          {midterm/35*100:.2f}%")
print(f"Final Exam       {final/50*100:.2f}%")

print("-"+"="*21+"-")

total = (assignment1/18*0.1 + assignment2/22*0.1 + assignment3/15*0.1 + assignment4/30*0.1 + midterm/35*0.25 + final/50*0.35)*100

print(f"Your final grade is {total:.2f}%.")

