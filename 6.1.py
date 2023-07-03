def get_primes_from_range(start, end):
    primes = []   
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num/2) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)   
    return primes