#!/usr/bin/env python3
"""Module for poisson distribution"""


class Poisson:
    """Class Poission"""
    def __init__(self, data=None, lambtha=1.):
        """Data Initialization"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        """PMF calculation"""
        if k < 0:
            return 0
        if not isinstance(k, int):
            k = int(k)
        k_factorial = 1
        if k != 0:
            for x in range(2, k+1):
                k_factorial = k_factorial * x
        return ((self.lambtha ** (k)) *
                (2.7182818285 ** (-(self.lambtha)))) / k_factorial

    def cdf(self, k):
        """CDF calculation"""
        if k < 0:
            return 0
        if not isinstance(k, int):
            k = int(k)
        CDF = 0
        for x in range(0, k+1):
            CDF = CDF + self.pmf(x)
        return CDF
