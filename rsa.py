import sys

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_prime_factors(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factor1 = i
            factor2 = n // i
            if is_prime(factor1) and is_prime(factor2):
                return (factor1, factor2)
    return None

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            n = int(line.strip())
            factors = find_prime_factors(n)
            print(f"{n}=", end="")
            if factors:
                print(f"{factors[0]}*{factors[1]}")
            else:
                print("No prime factors found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rsa.py <file>")
        sys.exit(1)
    main(sys.argv[1])

