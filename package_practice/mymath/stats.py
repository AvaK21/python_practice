def mean(numbers):
    """
    Function returns the mean of the list of numbers
    """
    return sum(numbers)/len(numbers)

def median(numbers):
    """
    Returns median of the given list
    """
    numbers.sort()

    if(len(numbers) % 2 == 0):
        median1 = numbers[len(numbers) // 2]
        median2 = numbers[len(numbers) //2 -1]
        mymedian = (median1 + median2) / 2
    else:
        mymedian = numbers[len(numbers) // 2]
    return mymedian
