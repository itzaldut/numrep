import numpy as np

def test_limits(dtype, signed=True):
    print(f"\n-- Testing {dtype} ({'signed' if signed else 'unsigned'}) --")
    
    # Determine the range for the given dtype
    if signed:
        max_val = np.iinfo(dtype).max
        min_val = np.iinfo(dtype).min
    else:
        max_val = np.iinfo(dtype).max
        min_val = 0

    print(f"Max value: {max_val}")
    print(f"Min value: {min_val}")

    # Overflow test
    near_max = max_val - 1
    overflow = near_max + 2
    print(f"near_max + 2 = {overflow}")

    # Underflow test (for signed types only)
    if signed:
        near_min = min_val + 1
        underflow = near_min - 2
        print(f"near_min - 2 = {underflow}")

def test_python_int():
    print("\n-- Testing Python int (arbitrary precision) --")
    max_val = 2**63 - 1
    min_val = -2**63
    print(f"Max value: {max_val}")
    print(f"Min value: {min_val}")

    # Overflow test
    near_max = max_val - 1
    overflow = near_max + 2
    print(f"near_max + 2 = {overflow}")

    # Underflow test
    near_min = min_val + 1
    underflow = near_min - 2
    print(f"near_min - 2 = {underflow}")

# Test NumPy fixed-size integers
test_limits(np.int32, signed=True)
test_limits(np.uint32, signed=False)
test_limits(np.int64, signed=True)
test_limits(np.uint64, signed=False)

# Test Python's arbitrary-precision int
test_python_int()

