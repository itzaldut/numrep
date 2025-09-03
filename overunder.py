import numpy as np
import sys
import math

def find_overflow_limit(dtype):
    x = dtype(1.0)
    while True:
        y = x * dtype(2.0)
        if math.isinf(float(y)):
            return x, y
        x = y

def find_underflow_limit(dtype):
    x = dtype(1.0)
    while True:
        y = x * dtype(0.5)
        if y == dtype(0.0):
            return x, y
        x = y

def main():
    # Double‑precision (Python's native float)
    print("=== Double precision (float64) ===")
    of_low_d, of_high_d = find_overflow_limit(np.float64)
    uf_high_d, uf_low_d = find_underflow_limit(np.float64)
    print(f"Overflow occurs around between {of_low_d:e} and {of_high_d}")
    print(f"Underflow to zero occurs between {uf_low_d:e} and {uf_high_d:e}")
    print()

    # Single‑precision (float32)
    of_low_s, of_high_s = find_overflow_limit(np.float32)
    uf_high_s, uf_low_s = find_underflow_limit(np.float32)
    print(f"Overflow occurs around between {of_low_s:e} and {of_high_s}")
    print(f"Underflow to zero occurs between {uf_low_s:e} and {uf_high_s:e}")

if __name__ == "__main__":
    main()

