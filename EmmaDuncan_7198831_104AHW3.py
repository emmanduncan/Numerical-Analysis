### Emma Duncan
### Math 104 A Homework 3
### Due: 27 October 2016

### code to create list of nodes
### inputs: n (number of nodes)

import math

#calculates nodes for given n, based on equations in part 3b x between [-1,1]
def nodelist(n):
    nodes = []
    for j in range(0,n+1):
        xj = -1 + j*(2/n)
        nodes.append(xj)
    return(nodes)

## function from part 3b
def fx2(x):
    return(math.exp(-(x**2)))

## calculates coefficients for interpolation polynomial
## first calculates c_j=f(x_j) for 0th order, then calculates rest of coefficients
## if coefficient is first in order (will be used for polynomial), places that value into "coeff" list
## all valuces of c_j coefficients are placed into "allc" list to be used to calculate subsequent coefficients

def coefficients(nodes, fx):
    allc=[]
    coeff=[]
    n=len(nodes)
    for j in range(0,n):
        cj=fx(nodes[j])
        if j==0:
            coeff.append(cj)
            allc.append(cj)
        else:
            allc.append(cj)
    for i in range (n-1,-1,-1):
        for k in range (0,i):
            cj=((allc[len(allc)-i]-allc[len(allc)-i-1])/(nodes[n-i+k]-nodes[k]))
            if k==0:
                coeff.append(cj)
                allc.append(cj)
            else:
                allc.append(cj)
    return(coeff)   

## code to calculate value of polynomial at given list of nodes
## inputs: x (degree for interpolation polynomial)
##         fx (function used to calculate coefficients)
##         nx (value used as nodes to plug into polynomial
## first calculates the list of xj values that will be used to calculate coefficients, then calculates the coefficients
## using for loop plugs into polynomial interpolation for each value of nx nodes (100 points x_j in 3b) and places into list
## Then returns list of P_10(x) for each x_j where j=nx (j=100 for 3b)

def polynomial(x,fx,nx):
    xj=nodelist(x)
    coeff=coefficients(xj, fx)
    n = len(coeff)
    pn = coeff[n-1]
    xnodes=[]
    x=nodelist(nx)
    for i in range(0,nx+1):
        for j in range (n-2,-1,-1):
            pn=coeff[j]+(x[i]-xj[j])*pn
        xnodes.append(pn)
    return(xnodes)

p10x= polynomial(10,fx2,100) #command to run test in 3b

#calculates error and places into list of values that can then be plotted
def error(fx,approx):
    errorlist=[]
    fxlist=[]
    for i in range(0,100):
        e = fx2(nodelist(100)[i])
        errorlist.append(e-approx[i])
    return (errorlist)


3a.
 

3b.
 
 
