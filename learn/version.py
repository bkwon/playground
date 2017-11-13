import sys

print(sys.version)
print("To Error is Divine")
print(5.5 * 6 // 2 + 8)

feet = 5280
miles = 13
print(miles * feet)

hours = 7
minutes = 21
seconds = 37
print("The number of seconds is " + str(hours*60*60 + minutes*60 + seconds) )


mass_in_ounces = 0
mass_in_grams = 1

mass_in_ounces = mass_in_grams * 0.035274

print(mass_in_ounces)

def useless(input1, input2, input3):
    return 3
useless(1,2,3)
print(useless(4,5,6))

result = useless(4,4,4)
print(result)
