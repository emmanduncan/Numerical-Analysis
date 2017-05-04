# Emma Duncan - 7198831 #
# Math 104A Homework 2 #
import numpy
import math

########################################################################
######################### CODE FOR PROBLEM 2 ###########################
########################################################################


### these are the data sets used in problem 1 and 2
### used as inputs to check Barycentric formula
x = [0,1,3]
fx = [1,1,-5]

data2b = numpy.array([0.00, 0.25, 0.50, 0.75, 1.25, 1.50])
data2b_fxj = numpy.array([0.0000, 0.7071, 1.0000, 0.7071, -0.7071, -1.0000])

### equation for Barycentric weights, lambda
### inputs: list of data sets for x_j, j
### takes x values and calculates each lambda_j

def lambda1(data,j):
    prod=1
    j=int(j)
    for xk in data:
        if data[j] != xk:
            dif = data[j] - xk
        else:
            dif=1
        prod = prod*dif
    return(1/prod)

### equation for Barycentric Formula
### inputs: x_j values, f(x_j) values, x-value
### output: P(x) value approximating f(x)

def Barycentric(xdata,ydata,x):
    sumtop=0
    sumbottom=0
    for i in range(0,(len(xdata))):
        sumtop+=((lambda1(xdata,i)/(x-xdata[i]))*(ydata[i]))
        sumbottom+=((lambda1(xdata,i))/(x-xdata[i]))
    return(sumtop/sumbottom)



########################################################################
######################### CODE FOR PROBLEM 3 ###########################
########################################################################


#################################### 3A #################################

#xlist and fxlist calculate and create lists for x_j and f(x_j) for the function in 3a
def xlist(n):   ### x_j ###
    data3a_xj=[]
    for i in range (0,n):
        x = -5 + i*(10/n)
        data3a_xj.append(x)
    return(numpy.array(data3a_xj))

def fxlist(n):   ### f(x_j) ###
    a=xlist(n)
    data3a_fxj=[]
    for i in range(0,len(a)):
        fx = 1/(1+a[i]**2)
        data3a_fxj.append(fx)
    return(numpy.array(data3a_fxj))
    

### adjusted lambda to reflect the even spacing of x_j's -- calculates binomial coefficent form of lambda
def lambda2(data, j):
    choose = (math.factorial(len(data)))/((math.factorial(len(data)-j))*math.factorial(j))
    return(((-1)**j)*(choose))

### Barycentric formula takes xlist and fxlist, uses binomial coefficient lambda to calculate Barycentric formula
def Barycentric2(xdata,ydata,x):
    sumtop=0
    sumbottom=0
    for i in range(0,(len(xdata)-1)):
        if xdata[i] != x:
            sumtop+=((lambda2(xdata,i)/(x-xdata[i]))*(ydata[i]))
            sumbottom+=((lambda2(xdata,i))/(x-xdata[i]))
    return(sumtop/sumbottom)

### data sets for n=4
list1x=xlist(4)
list1fx=fxlist(4)

### data sets for n=8
list2x=xlist(8)
list2fx=fxlist(8)

###data sets for n=12
list3x=xlist(12)
list3fx=fxlist(12)


#################################### 3B #################################

#xlist and fxlist calculate and create lists for x_j and f(x_j) for the function in 3b
def xlistb(n):    ### x_j ###
    data3b_xj=[]
    for i in range (0,n):
        x = 5* math.cos(i*math.pi/n)
        data3b_xj.append(x)
    return(data3b_xj)

def fxlistb(n):    ### f(x_j) ###
    a=xlistb(n)
    data3b_fxj=[]
    for i in range(0,len(a)):
        fx = 1/(1+a[i]**2)
        data3b_fxj.append(fx)
    return(data3b_fxj)

### data sets for n=4
list1xb=xlistb(4)
list1fxb=fxlistb(4)

### data sets for n=8
list2xb=xlistb(8)
list2fxb=fxlistb(8)

###data sets for n=12
list3xb=xlistb(12)
list3fxb=fxlistb(12)

### data sets for n=100
list4xb=numpy.array(xlistb(100))
list4fxb=numpy.array(fxlistb(100))
ppp = numpy.vstack((list4xb,list4fxb))

### adjusted lambda to reflect different form of x_j
def lambda3(data, j):
    if j==0 or j==len(data):
        l = (1/2)*((-1)**j)
    else:
        l = ((-1)**j)
    return (l)

### Barycentric formula with lambda3
def Barycentric3(xdata,ydata,x):
    sumtop=0
    sumbottom=0
    for i in range(0,(len(xdata)-1)):
        if xdata[i] != x:
            sumtop+=((lambda3(xdata,i)/(x-xdata[i]))*(ydata[i]))
            sumbottom+=((lambda3(xdata,i))/(x-xdata[i]))
        else:
            sumbottom+=0
            sumtop+=0
    return(sumtop/sumbottom)


###################################### 3C #################################


### xlist and fxlist calculate and create lists for x_j and f(x_j) for the function in 3c
def xlistc(n):   ### x_j ###
    data3c_xj=[]
    for i in range (0,n):
        x = -5 + i*(10/n)
        data3c_xj.append(x)
    return(data3c_xj)

def fxlistc(n):   ### f(x_j) ###
    a=xlistc(n)
    data3c_fxj=[]
    for i in range(0,len(a)):
        fx = math.exp(((-i)**2)/5)
        data3c_fxj.append(fx)
    return(data3c_fxj)

### adjusted lambda to reflect the even spacing of x_j's -- calculates binomial coefficent form of lambda
def lambda4(data, j):
    choose = (math.factorial(len(data)))/((math.factorial(len(data)-j))*math.factorial(j))
    return(((-1)**j)*(choose))

### Barycentric formula takes xlist and fxlist, uses binomial coefficient lambda to calculate Barycentric formula
def Barycentric4(xdata,ydata,x):
    sumtop=0
    sumbottom=0
    for i in range(0,(len(xdata)-1)):
        if xdata[i] != x:
            sumtop+=((lambda4(xdata,i)/(x-xdata[i]))*(ydata[i]))
            sumbottom+=((lambda4(xdata,i))/(x-xdata[i]))
    return(sumtop/sumbottom)

### data sets for n=4
list1xc=xlistc(4)
list1fxc=fxlistc(4)

### data sets for n=8
list2xc=xlistc(8)
list2fxc=fxlistc(8)

###data sets for n=12
list3xc=xlistc(12)
list3fxc=fxlistc(12)

