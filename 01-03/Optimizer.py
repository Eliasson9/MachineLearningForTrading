import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def fit_line(data, error_func):
    """
    
    :param data: 2D array where each row is a point (X0, Y)
    :param error_func: function that computes the error between a line and observed data
    :return: line that minimizes the error function
    """

    l = np.float32([0, np.mean(data[:, 1])])

    x_ends = np.float32([-5, 5])
    plt.plot(x_ends, l[0] * x_ends + l[1], 'm--', linewidth=2.0, label="Initial guess")

    return spo.minimize(error_func, l, args=(data,), method='SLSQP', options={'disp': True}).x

def fit_poly(data, error_func, degree=3):
    Cguess = np.poly1d(np.ones(degree + 1, dtype=np.float32))

def error(line, data):
    """
    
    :param line: tuple/list/array (C0, C1) where C0 is slope and C1 is Y-intercept
    :param data: 2D array where each row is a point (x, y)
    :return: error as a single real value
    """

    # Sum of squared Y-axis differences
    err = np.sum((data[:, 1] - (line[0] * data[:, 0] + line[1])) ** 2)
    return err

def error_poly(C, data):
    """
    
    :param C: numpy.pol1d obj or equivalent array representing polynomial coefficients
    :param data: 2D array where each row is a point (x, y)
    :return: error as a single real value   
    """

    # Sum of squared Y-axis differences
    return np.sum((data[:, 1] - np.polyval(C, data[:, 0])) ** 2)

def f(x):
    y = (x - 1.5) ** 2 + 0.5
    print "x = {}, y = {}".format(x, y)
    return y


def test_run():
    l_orig = np.float32([4, 2])

    print "Original line: C0 = {}, C1 = {}".format(l_orig[0], l_orig[1])

    Xorig = np.linspace(0, 10, 21)
    # kx + m
    Yorig = l_orig[0] * Xorig + l_orig[1]

    plt.plot(Xorig, Yorig, 'b', linewidth=2.0, label="Original line")

    # Gerenerate noisy data
    niose_sigma = 3.0
    noise = np.random.normal(0, niose_sigma, Yorig.shape)
    data = np.asarray([Xorig, Yorig + noise]).T
    plt.plot(data[:, 0], data[:, 1], 'go', label="Data points")

    # Fit line to data
    l_fit = fit_line(data, error)
    print "Fitted line: C0 = {}, C1 = {}".format(l_fit[0], l_fit[1])
    plt.plot(data[:, 0], l_fit[0] * data[:, 0] + l_fit[1], 'r--', linewidth=2.0, label="Fitted line")
    plt.legend(loc='upper left')
    plt.show()
    Xguess = 2.0

    min_result = spo.minimize(f, Xguess, method='SLSQP', options={'disp': True})
    print "Minima found at:"
    print "x = {}, y = {}".format(min_result.x, min_result.fun)


if __name__ == "__main__":
    test_run()
