# ASM-Bayes
code for the assignment 1 of the course Applied Statistical Methods (Baye's group)

## Description
Alice and Bob are measuring the average wind speed during a cyclone. They have a machine that gives them hourly wind speed reading. From previous experience, they know that the average wind speed is between 62 to 88 km/h. They want to know the actual wind speed during the cyclone and they have 4 machines that independently give 10, 20, 50 and 100 readings respectively. Now Alice is a frequentist while Bob believes in the Bayesian method. They both use statistical inference to find out 95% confidence intervals for the wind speed.
Alice models the readings as normal distribution and derives a 95% confidence interval using the standard normal distribution; Bob also models the readings as a normal distribution but he can do better! He knows that the wind speed is generally between 62 and 88km/h and thus he assumes a prior distribution of N(75,16) and updates the distribution with each new data point. Thus, Bob's estimates have relatively less variance than Alice's and he gets very accurate estimates even with only 10 data points.

Their results are shown in the figure given below. The blue curve represents the distribution of the original data (with a mean of 79.3 and a standard deviation of 0.3) while the red and yellow lines represent 95% confidence intervals for the frequentist and bayesian approaches respectively.

## Output
![](output.png)
![](graph.png)
