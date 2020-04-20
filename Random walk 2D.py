import numpy
import pylab
import random

#no of steps
n = 100000

#arrays for x and y coordinates using numpy
xcor = numpy.zeros(n)
ycor = numpy.zeros(n)

#filling coordinates with random variables
for i in range (1,n):
    val = random.randint(1,4)
    if val == 1:
        xcor[i] = xcor[i - 1] + 1
        ycor[i] = ycor[i - 1]
    elif val == 2:
        xcor[i] = xcor[i - 1] - 1
        ycor[i] = ycor[i - 1]
    elif val == 3:
        xcor[i] = xcor[i - 1]
        ycor[i] = ycor[i - 1] + 1
    elif val == 4:
        xcor[i] = xcor[i - 1]
        ycor[i] = ycor[i - 1] - 1

#plotting the walk
pylab.title("Random Walk 2D ($n = " + str(n) + "$ steps)")
pylab.plot(xcor, ycor)
#for saving your result as an image
pylab.savefig("rand_walk_2D_result"+str(n)+".png",bbox_inches="tight",dpi=600)
pylab.show()
