def sayhello():
    """Prints Hello"""
    print("Hello")

sayhello()

def double(x):
    return x*2

def product(val1, val2, val3):
    # print("The product of your 3 inputs is " + str(val1*val2*val3))
    prod = val1 * val2 * val3
    print(prod)
    prod = val1*prod + 1
    print(prod)
    return prod

result = product(1, 1, 1977)
print(result)

print('she shouted "Hello!" very loudly')

#
# double_result = double(result)
# print(double_result)
# print("Your double result is " + str(double_result))

