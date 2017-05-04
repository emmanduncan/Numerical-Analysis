# Emma Duncan
# Math 104 Homework 1
# 6 October 2016

import math

# need to define functions that we will estimate using CTR function below
# f3 is for #3, f4 is for #4

def f3(x):
    return(x*math.exp(x**2))
def f4(x):
    return(math.exp(-x**2))
    
#this is the Composite Trapezoidal Rule quadrature calculation
#Inputs:f(function we are using), a(lower bound), b(upper bound), N
#the CTR function will output the T(f) value for a given h (calculated in the function using a,b,N)
def CTR(f,a,b,N):
    total = 0
    h = (b-a)/N
    total += (1/2)*h*f(a)
    for i in range(1,N):
        total += h*f(a+i*h)
    total += (1/2)*h*f(b)
    return(total)
    
#CTR(0,1,10) = 0.6627781133777506
#CTR(0,1,20) = 0.7435070723552096
#CTR(0,1,40) = 0.7964474327319483

# To find error calculate: Error = |I(f)-T(f)|
# From solving definite integral: I(f) = 0.85914

#q(N) function calculates the ratio which indicates if h is sufficiently small, and if the estimate of error is accurate
#Use N=1/h as input
#Output should be approximately 4
def q(N): 
    return ((CTR(f4,0,1,N*2)-CTR(f4,0,1,N))/(CTR(f4,0,1,N*4)-CTR(f4,0,1,N*2)))

#s(N) calculates extrapolated, improved approximation
#use N=1/h as input
#expected output should be closer to true value of integral than CTR
def s(N):
    return(CTR(f4,0,1,N)+(4/3)*(CTR(f4,0,1,N*2)-CTR(f4,0,1,N)))


