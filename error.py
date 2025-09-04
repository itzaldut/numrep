import numpy as np
import matplotlib.pyplot as plt

# Functions and their derivatives
funcs = [
    (np.cos, lambda t: -np.sin(t), 'cos'),
    (np.exp, np.exp, 'exp')
]
t_values = [0.1, 1.0, 100.0]
methods = {
    'forward': lambda f, t, h: (f(t + h) - f(t)) / h,
    'central': lambda f, t, h: (f(t + h) - f(t - h)) / (2*h),
    'richardson': lambda f, t, h: (-3*f(t) + 4*f(t+h) - f(t+2*h)) / (2*h)
}
h_space = np.logspace(-16, -1, 100)

for f, df, fname in funcs:
    for t in t_values:
        plt.figure()
        for method_name, method in methods.items():
            errs = []
            for h in h_space:
                approx = method(f, t, h)
                exact = df(t)
                rel_err = abs((approx - exact) / exact) if exact != 0 else abs(approx - exact)
                errs.append(rel_err)
            plt.loglog(h_space, errs, label=method_name)
        plt.xlabel('h')
        plt.ylabel('Relative Error')
        plt.title(f'rel error vs h at t={t} for {fname}')
        plt.legend()
        plt.savefig(f'{fname}_{t}_error.png')

