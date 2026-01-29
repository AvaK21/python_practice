"""THis is a test of using pylint library, first install pylint and
then run the command pylint "filename"""



def add(number1, number2):
    """returns the sum of the parameters"""
    return number1 + number2

NUM1 = 4

NUM2 = 5

"""Result is addition operation of the arguements NUM1 and NUM2"""
TOTAL = add(NUM1, NUM2)

print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
