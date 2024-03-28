import sys

def factorize(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            n = int(line.strip())
            factors = factorize(n)
            print(f"{n}=", end="")
            if factors:
                print(f"{factors[0][0]}*{factors[0][1]}")
            else:
                print(f"{n}*1")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        sys.exit(1)
    main(sys.argv[1])

