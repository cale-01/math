# >find the largest possible prime number such that if you remove any digit from that number, it stays a prime number
# >to make it more interesting, any two adjacent digits in that number cannot be the same


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

def find_largest_prime():
    prime = 1000000  # Starting with a large prime number // change this parameter
    
    while prime > 0:
        prime_str = str(prime)
        
        if all(is_prime(int(prime_str[:i] + prime_str[i+1:])) for i in range(len(prime_str))):
            if all(prime_str[i] != prime_str[i+1] for i in range(len(prime_str)-1)):
                return prime
        prime -= 1

largest_prime = find_largest_prime()
print("The largest prime number that satisfies the given conditions is:", largest_prime)

find_largest_prime()