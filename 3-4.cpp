#include <iostream>
#include <limits>
#include <climits>

template<typename T, bool is_signed>
void test_limits(const std::string& name) {
    std::cout << "\n-- Testing " << name << " (" 
              << (is_signed ? "signed" : "unsigned") << ") --\n";
    T maxv = std::numeric_limits<T>::max();
    T minv = std::numeric_limits<T>::min();
    std::cout << "Max value: " << maxv << "\n"
              << "Min value: " << minv << "\n";

    // Overflow test
    T near_max = maxv - 1;
    T ov = near_max + 2;  // potentially wraps
    std::cout << "near_max + 2 = " << ov << "\n";

    // Underflow test (for signed only)
    if (is_signed) {
        T near_min = minv + 1;
        T uv = near_min - 2;  // potentially wraps
        std::cout << "near_min - 2 = " << uv << "\n";
    }

    std::cout << std::endl;
}

int main() {
    test_limits<int, true>("int");
    test_limits<unsigned int, false>("unsigned int");
    return 0;
}

