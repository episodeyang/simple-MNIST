import numpy as np


def σ(xs):
    return 1 / (1 + np.exp(-xs))


if __name__ == "__main__":
    xs = np.linspace(0, 1, 20)
    print(np.shape(xs))

    a_s = σ(xs)
    print(np.shape(a_s))
    print(a_s)
