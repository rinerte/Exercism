def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    divisors = get_divisors(number)
    if sum(divisors)==number:
        return "perfect"
    elif sum(divisors)<number:
        return "deficient"
    return "abundant"
    
def get_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors