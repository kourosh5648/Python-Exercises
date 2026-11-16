
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
 
mu = 0
sigma = 1
 
x = np.linspace(-4, 4, 1000)
 
y = norm.cdf(x, loc=mu, scale=sigma)
 
plt.plot(x, y)

plt.title("Gaussian Cumulative Distribution Function")
plt.xlabel("X")
plt.ylabel("CDF")

plt.grid()
plt.show()
