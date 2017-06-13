from numpy import arange,array,ones,linalg
from pylab import plot,show

x = arange(0,9)
A = array([ x, [1,1,1,1,1,1,1,1,1]])

y = [3, 4, 5, 6, 6.5, 7, 8, 9.5, 10]
w = linalg.lstsq(A.T,y)[0]

line = w[0]*x+w[1] # regression line
plot(x,line,'r-',x,y,'o')
show()

#http://glowingpython.blogspot.kr/2012/03/linear-regression-with-numpy.html
