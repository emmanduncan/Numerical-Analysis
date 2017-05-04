# Emma Duncan
# Math 104A Homework 4
# 10 November 2016

### code to calculate z coefficients ###
### inputs: n, xlist, ylist ############

tlist=[0,0.618,0.935,1.255,1.636,1.905,2.317,2.827,3.330]
xlist=[1.50,0.90,0.60,0.35,0.20,0.10,0.50,1.00,1.50]
ylist=[0.75,0.90,1.00,0.80,0.45,0.20,0.10,0.20,0.25]
n=len(tlist)


###############################################################################
###### This code calculates all of the coefficients for the spline function, and estimates the value of the function for a given x
###### INPUTS: n (number of values), xlist(list of x values), ylist(list of y values), x(value to evaluate interpolation formula at)
###### OUTPUTS: list of coefficients for each piece-wise portion of the spline interpolation, S(x) value

def allcoeff(n,xlist,ylist,x):
# first part of code calculates z coefficients #
    h=[]
    b=[]
    u=[]
    v=[]
    z=[]
    for i in range(0,n-1):
        h.append(xlist[i+1]-xlist[i])
        b.append(6*(ylist[i+1]-ylist[i])/h[i])
    u.append(2*(h[0]+h[1]))
    v.append(b[1]-b[0])
    for i in range (2,n-1):
        u.append((2*(h[i]+h[i-1]))-(((h[i-1])**2)/(u[i-2])))
        v.append(b[i]-b[i-1]-h[i-1]*v[i-2]/u[i-2])
    for i in range(n):
        z.append(0)
    for i in range (n-2,0,-1):
        z[i]=(v[i-2]-(h[i]*z[i+1]))/u[i-2]
# next calculates each a,b,c,d for each segment [x_j,x_j+1] #
    alllist=[]
    for i in range(0,n-1):
        coefflist=[]
        aj=(1/(6*h[i]))*(z[i+1]-z[i])
        coefflist.append(aj)
        bj=(1/2)*z[i]
        coefflist.append(bj)
        cj=(1/h[i])*(ylist[i+1]-ylist[i])-(1/6)*h[i]*(z[i+1]-2*z[i])
        coefflist.append(cj)
        dj=ylist[i]
        coefflist.append(dj)
        alllist.append(coefflist)
    print(alllist)
# evaluates interpolation at x, finds [x_j,x_j+1] where x belongs in and evaluates with correct coefficients a,b,c,d #
    for i in range(n-1):
        if xlist[i]<=x<xlist[i+1]:
            j=i
    s=alllist[j][0]*(x-xlist[j])**3+alllist[j][1]*(x-xlist[j])**2+alllist[j][2]*(x-xlist[j])+alllist[j][3]
    return(s)


######### 2 #########
### for #2, I used the list of coefficients for (t,x) and (t,y) to plot the parametric equation
### See table of coefficients for spline function (t_j,x_j) and (t_j,y_j)
### See graph of parametric spline function



