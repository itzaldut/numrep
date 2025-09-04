import numpy as np
import matplotlib.pyplot as plt
import math

# Define functions
funcs = [
    (np.cos, lambda t: -np.sin(t), 'cos'),
    (np.exp, np.exp, 'exp')
]

methods = {
    'forward': lambda f, t, h: (f(t + h) - f(t)) / h,
    'central': lambda f, t, h: (f(t + h) - f(t - h)) / (2*h),
    'richardson': lambda f, t, h: (-3*f(t) + 4*f(t+h) - f(t+2*h)) / (2*h)
}

t0 = 0.1  # Fixed t for both plots
h_space = np.logspace(-15, -1, 200)

for f, df, fname in funcs:
    plt.figure()
    for method_name, method in methods.items():
        errs = []
        for h in h_space:
            approx = method(f, t0, h)
            exact = df(t0)
            rel_err = abs((approx - exact) / exact) if exact != 0 else abs(approx - exact)
            errs.append(rel_err)
        plt.loglog(h_space, errs, label=method_name)
    
    # Optional: annotate slopes, optimal h
    plt.xlabel('Step size $h$')
    plt.ylabel('Relative Error')
    plt.title(f'Relative Error vs $h$ for {fname}(t), t = {t0}')
    plt.legend()
    plt.grid(True, which='both', ls='--')
    plt.savefig(f'{fname}.png')
    plt.close()

