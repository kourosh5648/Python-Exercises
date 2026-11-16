
import math

def phi(z):
    return math.exp(-z*z/2) / math.sqrt(2*math.pi)


def Phi(z):

    if z < -8.0:
        return 0.0

    if z > 8.0:
        return 1.0

    total = 0.0
    term = z
    i = 3

    while total != total + term:
        total += term
        term *= z * z / float(i)
        i += 2

    return 0.5 + phi(z) * total


def cdf(z, mu=0.0, sigma=1.0):
    return Phi((z - mu) / sigma)


print(cdf(0))
print(cdf(1))
print(cdf(2))
