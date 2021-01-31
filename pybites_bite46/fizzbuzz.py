def fizzbuzz(num):
    primes = {3: "Fizz", 5: "Buzz"}

    result = [word for prime, word in primes.items() if num % prime == 0]
    if result:
        return " ".join(result)
    else:
        return num
