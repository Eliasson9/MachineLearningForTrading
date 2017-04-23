import numpy as np
import matplotlib.pyplot as plt

scores = [3.0, 1.0, 0.2]

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    dist = np.exp(x) / np.sum( np.exp(x), axis = 0)
    return dist

# Plot softmax curves
if __name__ == '__main__':
    x = np.arange(-2.0, 6.0, 0.1)
    scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])


    print(softmax(scores/10))
    plt.plot(x, softmax(scores / 10).T, linewidth=2)
    plt.show()