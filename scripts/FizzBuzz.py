def fizzbuzz(count):
    """FizzBuzz implementation
    Returns list of output messages.
    """
    if not isinstance(count, int):
        raise TypeError('count must be an integer')
    if count < 1 or count > 1000:
        raise ValueError('count must be between 1 and 1000')
    results = []
    for num in range(1, count+1):
        if num % 3 == 0 and num % 5 == 0:
            results.append('FizzBuzz')
        elif num % 3 == 0:
            results.append('Fizz')
        elif num % 5 == 0:
            results.append('Buzz')
        else:
            results.append(str(num))
    return results
