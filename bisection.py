#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 00:25:14 2019

@author: Abdulkadir Kahraman, Süleyman Tarsuslu
"""


import numpy as np



"""
% Program 1.1 Bisection Method
% Computes approximate solution of f(x)=0
% Input: function handle f; a,b such that f(a)*f(b)<0,
%        and tolerance tol defaultly tol=10e-6
% Output: Approximate solution c 
"""
def bisection(f,a,b,tol=10**-5):
    c=0
    itr=0
    while abs(b-a)/2 > tol:
        c=(a+b)/2
        #print (itr,a,c,b,(b*c<0))
        if f(c)*f(a)<0:
            b=c
        else:
            a=c
        itr+=1
    #print (itr,a,c,b)
    return itr,c

# Returns step number to reach the desired accuracy
def step(a,b,ac):
    er=(b-a)/(0.5*10**(-1*ac))
    return np.ceil(np.log2(er)-1)
    
# Sample functions for test 
#f=lambda x: x**3+x-1
#f=lambda x: cos(x)-x
#f=lambda x: x**3-9
#f=lambda x: x**3-2*x**2+4*x/3-8/27
f=lambda x: np.cos(x)-np.sin(x)

# Test the bisection method
a=0
b=1
st=step(a,b,3)
itr,c=bisection(f,a,b,10**-3)
