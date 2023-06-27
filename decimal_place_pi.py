import decimal
import math

def calculate_pi(digits):
    decimal.getcontext().prec = digits + 2  # Set precision for Decimal module

    # Chudnovsky algorithm to calculate Pi
    C = 426880 * decimal.Decimal(10005).sqrt()
    K = decimal.Decimal(6)
    X = decimal.Decimal(1)
    M = decimal.Decimal(1)
    L = decimal.Decimal(13591409)
    S = L

    for i in range(1, digits//14 + 1):
        M = M * (K**3 - 16 * K) // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X

    pi = C / S
    return str(pi)[:-1]  # Remove the last digit to match requested precision

# Main program
digits = int(input("Enter the number of decimal places for Pi: "))
pi_value = calculate_pi(digits)
print("Pi to", digits, "decimal places:")
print(pi_value)
