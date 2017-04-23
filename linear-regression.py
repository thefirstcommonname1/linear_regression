import numpy as np
x = [0,0.5,1,2,4,3,5]
y = [50,70,72,78,92,82,100]
N = len(y)
alpha = 0.0001
theta0 = 0
theta1 = 0

def cost_function(theta0, theta1):
    error = 0
    for i in range(N):
        error += ((theta1 * x[i] + theta0) - y[i]) ** 2
    return error/2*float(N)

def gradient_descent(theta0, theta1):
    for i in range(1000): #number of times performing gradient_descent
        theta0 , theta1 = helper_function(theta0, theta1)
    return (theta0, theta1)

def helper_function(theta0, theta1):
    #repeat until convergence
    theta0_partial_derivative = 0
    theta1_partial_derivative = 0
    for i in range(0, N):
        theta0_partial_derivative += 1/N * (theta1 * x[i] - y[i])
        theta1_partial_derivative += 1/N * (theta1 * x[i] - y[i]) * x[i]
    theta0 = theta0 - alpha * theta0_partial_derivative
    theta1 = theta1 - alpha * theta1_partial_derivative
    return (theta0, theta1)

theta0, theta1 = gradient_descent(theta0, theta1)
print("The best fit slope is {} and the intercet is {}".format(theta0, theta1))
print("Error rate: {}".format(cost_function(theta0, theta1)))
