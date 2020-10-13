import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Data
alpha = 0.05
true_mean = 79.3
true_std = 0.3
print(f'True mean: {true_mean} | True std {true_std}')

for i,n in enumerate([10,20,50,100]):
    x = np.random.normal(loc=true_mean, scale=true_std, size=n)

    ### Frequentist model - Confidence interval ###
    x_bar = np.sum(x)/n
    z = norm.ppf(1-alpha/2)
    freq_left = round(x_bar - z*true_std/np.sqrt(n), 3)
    freq_right = round(x_bar + z*true_std/np.sqrt(n), 3)
    print('')
    print(f'n = {str(n).zfill(3)} | 95% confidence interval for mean: ({freq_left}, {freq_right})')

    ### Bayesian model - Credible interval ###
    """
    References:
        * https://stats.stackexchange.com/questions/82292/example-of-real-life-use-of-bayesian-inference-on-mu-from-a-normal-distribu
        * Casella, G. (1985). An Introduction to Empirical Bayes Data Analysis. The American Statistician, 39(2), 83-87.
    """
    # prior distribution
    prior_mean = 75
    prior_std = 4

    tau = 1/true_std**2
    b = 1/prior_std
    x_bar = np.sum(x)/n

    # posterior distribution
    theta_mean = (prior_mean*b + x_bar*n*tau) / (b + n*tau)
    theta_std = np.sqrt(1 / (b + n*tau))
    z = norm.ppf(1-alpha/2)

    bayesian_left = round(theta_mean - z*theta_std/np.sqrt(n), 3)
    bayesian_right = round(theta_mean + z*theta_std/np.sqrt(n), 3)

    print(f'n = {str(n).zfill(3)} | 95% credible interval for mean: ({bayesian_left}, {bayesian_right})')

    ### Plot the results ###
    plt.subplot(2,2,i+1)
    plt.title(f'Analysis with {n} data points')
    x_ = np.linspace(true_mean - 5*true_std, true_mean + 5*true_std, 500)
    y_ = norm.pdf(x_, loc=true_mean, scale=true_std) # true normal distribution
    plt.plot(x_, y_, label='original data')
    plt.vlines(true_mean, min(y_), max(y_), colors='k', label='true mean', zorder=2)
    plt.hlines(0.005,freq_left, freq_right, color='r', label='frequentist interval')
    plt.hlines(0.007,bayesian_left, bayesian_right, color='y', label='bayesian interval')
    plt.legend(loc="lower right")
    plt.tight_layout()
plt.show() # display all the graphs
