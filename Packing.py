# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:22:32 2020

@author: hssharadga
"""
# inputs
############################
maxIterations = 1E6;
W=2438; 
H=W/2;  
densityDesired = 0.4
Radius = 50
minGap= 10 ## gab between circle
borderGap = 25 ## gab between border and the nearest circle
################################################

import numpy as np
from math import sqrt, pi

area = W*H;
# Add a Border Around Default Panel Size
xMin = borderGap
xMax = W-borderGap
yMin = borderGap
yMax = H-borderGap
areaBorder = (xMax-xMin)*(yMax-yMin)
densityBorder = 0


# inital circcle
x=np.random.randint (xMin+Radius,xMax-Radius)
y=np.random.randint (yMin+Radius, yMax-Radius)
r=Radius
Center=np.array ([[x,y]])


combinedRadius = 2*r
b=0
iterations = 0;

# Begin Adding Circles and Detect Overlaps
while densityBorder < densityDesired:
# Generate a New Circle

    xNew_=np.random.randint (xMin+Radius,xMax-Radius)
    yNew_=np.random.randint (yMin+Radius, yMax-Radius)
    New_Center= np.array ([xNew_,yNew_])

#Test if Circle Overlaps any Pre-Existing Circle with a Gap
    for a in Center:
        a=np.array(a)
        disBetweenCircles= sqrt((New_Center[0]-a[0])**2+(New_Center[1]-a[1])**2)
        
        if disBetweenCircles-combinedRadius<=minGap:
            b=b+1
    if b==0:
         Center=np.vstack ((Center,New_Center))
    else:
         b=0
         continue
            
            
            

    areaCovered=(len(Center))*pi*r**2;
    density = areaCovered/area;
    densityBorder = areaCovered/areaBorder;
    iterations=iterations+1;
    
    if iterations > maxIterations:
        break
    
print ('densityBorder:',densityBorder * 100)
print ('number of sphere: ',len(Center))
print ('number of iteration :',iterations)

#Saving the results in a file
with open('Circels.csv', "w", newline = '') as output: ## Circles is the name of excel file that will be produced
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(Center) ## Center is waht I want the python to write out

