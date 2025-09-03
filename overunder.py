import sys
import math

def find_overflow_limit():
    x = 1.0
    # Double the value until we hit infinity
    while True:
        y = x * 2.0
        if math.isinf(y):
            return x, y
        x = y

def find_underflow_limit():
    x = 1.0
    # Halve the value until it underflows to zero
    while True:
        y = x * 0.5
        if y == 0.0:
            return x, y
        x = y

def main():
    print("System float_info.max:", sys.float_info.max)
    print("System float_info.min (smallest positive normalized):", sys.float_info.min)
    print()

    of_low, of_high = find_overflow_limit()
    print(f"Overflow occurs between {of_low:.6e} and {of_high:.6e}")

    uf_high, uf_low = find_underflow_limit()
    print(f"Underflow (to zero) occurs between {uf_low:.6e} and {uf_high:.6e}")

if __name__ == "__main__":
    main()

