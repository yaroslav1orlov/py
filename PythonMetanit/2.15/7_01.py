numbers = [1, 10, 100, 1000, 12, 203, 123, 4321, 10000, 32, 1233, 4342, 43232, 223323424]
def finderOfBidestNumb():
    max = numbers[0]
    count = len(numbers)
    for i in range(count):
        if max < numbers[i]:
            max = numbers[i]
    return max

print(finderOfBidestNumb())