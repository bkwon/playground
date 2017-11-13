def cube_root(val):
    """
    Given number, return the cube root of the number
    """
    return val ** (1 / 3)

print(cube_root(8.0))
print(cube_root(64))


def max_of_2(val1, val2):
    if val1 > val2:
        return val1
    else:
        return val2

def max_of_3(val1, val2, val3):
    return max_of_2(val1, max_of_2(val2, val3))


def project_to_distance(point_x, point_y, distance):
    dist_to_origin = (point_x ** 2 + point_y ** 2) ** 0.5
    scale = distance / dist_to_origin
    print(point_x * scale, point_y * scale)

project_to_distance(2, 7, 4)

def do_stuff():
    """
    Example of print vs. return
    """
    print("Hello world")
    return "Is it over yet?"
    print("Goodbye cruel world!")

print(do_stuff())

'''
playing with math function, inputs and outputing max value from list array
'''
def f(x):
    return -5*x**5 + 67*x**2 - 47

v1 = f(0)
v2 = f(1)
v3 = f(2)
v4 = f(3)
list = [f(0), f(1), f(2), f(3)]
print("Max value of this functon is: ", max(list))

'''
Playing with compound interest scenario
'''
def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.
    future_value = present_value * (1 + rate_per_period)**periods
    return future_value

print("$1000 at 2% compounded daily for 4 years yields $", future_value(1000, .02, 365, 4))
print(future_value(500,.04,10,10))


'''
Compute Area of an Equilateral Triangle given length of one of its sides
'''
def equilateral(l):
    area = (3**.5)/4 * l**2
    return area
#print(equilateral(2))
print(equilateral(5))
print("Side length of 5 has area of: " + str(equilateral(5)))
