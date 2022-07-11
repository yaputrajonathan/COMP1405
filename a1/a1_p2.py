#Jonathan.
#101161272

distance = int(input("Enter a distance in cm: "))

feet = (distance / 30.48)

inch = (float(feet)*12)

x = (float(inch) - (int(feet)*12)) 

print(f"{distance}cm is approximately {int(feet - x/12)}\'{round(x)}\"")