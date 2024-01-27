# Classify Numbers According To Aliquot Sums
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # Handle Zero and Negative Integers
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    # Get Factors
    factors = [x for x in range(1, number) if number % x == 0]
    factors_sum = sum(factors)

    # Check
    if factors_sum == number:
        return 'perfect'
    elif factors_sum < number:
        return 'deficient'
    elif factors_sum > number:
        return 'abundant'
