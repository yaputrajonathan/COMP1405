#Jonathan.
#101161272

a = int(input("Enter side length a: "))
b = int(input("Enter side length b: "))
c = int(input("Enter side length c: "))

S = (a+b+c)/2
Area = (S*(S - a)*(S - b)*(S - c))**0.5

print(f"A triangle with side lengths {a}, {b}, and {c} has an area of {Area:.4f}")
