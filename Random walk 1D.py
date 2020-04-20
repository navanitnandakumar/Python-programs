import numpy
import matplotlib.pyplot as plt

#probability to move up or down
prob = [ 0.05 , 0.95 ]

#defining starting position
start = 3
position = [start]

#generating random points
r = numpy.random.random(1000)
down_p = r < prob[0]
up_p = r > prob[1]

#movement
#using zip to combine the randomly generated sequences
for idown_p, iup_p in zip(down_p, up_p):
    down = idown_p and position[-1] > 1
    up = iup_p and position[-1] < 4
    position.append(position[-1] - down + up)

#plotting the walk
plt.plot(position)
plt.show()
